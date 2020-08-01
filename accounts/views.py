from allauth.account.utils import complete_signup
from allauth.account.adapter import get_adapter
from allauth.account import signals
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, FormView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from django.utils.http import is_safe_url, url_has_allowed_host_and_scheme
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from datetime import datetime

from .forms import LoginForm, RegisterForm, GuestForm, ProfileForm, AddEmailForm
from .models import User, Profile, Photographer

from allauth.account.utils import perform_login

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    # from_email = request.POST.get('from_email', '')
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['admin@example.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponseRedirect('/contact/thanks/')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')
    return HttpResponse('Make sure all fields are entered and valid.')


@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('/'))



# Will be replaced by the classbase LoginView when the bug is fixed
def login_page(request):
    if request.user.is_authenticated:
        if request.user.tier.tier < 3:
            return redirect("/?role=pri")
        else:
            return redirect("/?role=cur")

    form = LoginForm(request.POST or None)
    context = {
        "form": form, 'namespace':'accounts',
        # 'site_key': settings.RECAPTCHA_SITE_KEY,
    }
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    # if redirect_path == '/': redirect_path = '/dashboard/'

    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        token_id = request.POST.get('token_id')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                del request.session['guest_email_id']
            except:
                pass
            # update the redirect_path here
            if user.is_active:
                if user.email:
                    return perform_login(request, user, email_verification=settings.ACCOUNT_EMAIL_VERIFICATION,
                                         redirect_url=redirect_path)
                else:
                    request.session['email_user'] = user.id
                    return redirect('set_email')

            if is_safe_url(redirect_path, request.get_host()):
            # if url_has_allowed_host_and_scheme(redirect_path, request.get_host()):
                return redirect("/detail/myphoto_browse_spc/?role=pri&display=checked")
                # return redirect(redirect_path)
            else:
                return redirect("/?role=pri")
                # return redirect("dashboard/")
        else:
            # Return an 'invalid login' error message.
            print("LOGIN FAIL:  Someone is trying to login and failed!")
            print("LOGIN FAIL:  Username: {} and password: {}".format(username, password))
            form.add_error(None, 'invalid username or password')
            context['form'] = form
            return render(request, "accounts/login.html", context)
    else:
        return render(request, "accounts/login.html", context)


def register_page(request):
    registered = False
    if request.method == "POST":
        user_form = RegisterForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)
        # context = {
        #     "user_form": user_form,
        #     "profile_form": profile_form,
        #     "registered":registered, 'namespace':'accounts',
        # }
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            # user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.created_date = timezone.now()
            # if 'profile_pic' in request.FILES:
            #     profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
            return complete_signup(
                request, user,
                settings.ACCOUNT_EMAIL_VERIFICATION,
                reverse_lazy('login'))
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = RegisterForm()
        profile_form = ProfileForm()

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "registered": registered, 'namespace':'accounts',
    }
    return render(request, "accounts/register.html", context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form, 'namespace':'accounts',
    })

class SetEmailView(FormView):
    template_name = 'account/set_email.html'
    form_class = AddEmailForm
    success_url = reverse_lazy('account_email_verification_sent')

    def get_user(self):
        user_id = self.request.session.get('email_user')
        user = User.objects.get(id=user_id)
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        user = self.get_user()
        kwargs['user'] = user
        return kwargs

    def form_valid(self, form):
        user = self.get_user()
        email_address = form.save(self.request, user)
        get_adapter(self.request).add_message(
            self.request,
            messages.INFO,
            'account/messages/'
            'email_confirmation_sent.txt',
            {'email': form.cleaned_data["email"]})
        # signals.email_added(
        #     request=self.request,
        #     user=user,
        #     email_address=email_address)
        signals.email_added.send(sender=user.__class__,
                                 request=self.request,
                                 user=user,
                                 email_address=email_address)
        return super().form_valid(form)




class UpdateProfileView(LoginRequiredMixin, FormView):
    template_name = "accounts/update_profile.html"
    login_url = '/login/'
    model = Profile
    form_class = ProfileForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # this has all the form info
        context.update({'namespace': 'accounts'})

        return context

    def get_form(self, form_class=None):
        # do not need this one if using UpdateView
        if not form_class:
            form_class = self.get_form_class()
        if self.request.user.profile:

            form = form_class(instance=self.request.user.profile, **self.get_form_kwargs())
        else:
            form = form_class(**self.get_form_kwargs())
        return form

    def form_valid(self, form):
        profile = form.save(commit=False)
        if not profile.user:
            profile.user = self.request.user
        profile.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_invalid(form)


