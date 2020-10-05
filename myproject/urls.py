"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_page, register_page, send_email, UpdateProfileView, SetEmailView, ChangeEmailView, \
    PasswordChangeRedirect
from myproject.views import orchid_home, home, private_home
urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', home, name='home'),
    path('', orchid_home, name='orchid_home'),
    # path('index/', index, name='index'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('set_email/', SetEmailView.as_view(), name='set_email'),
    path('change_email/', ChangeEmailView.as_view(), name='change_email'),
    path('update_profile/', UpdateProfileView.as_view(), name='update_profile'),
    path('logout/', LogoutView.as_view(), {'next_page': '//'}, name='logout'),
    path('accounts/password/change/', PasswordChangeRedirect.as_view(), name="account_password_change"),
    path('accounts/', include('allauth.urls')),
    # path('password_reset/', include(password_reset.urls)),

    path('search/', include('search.urls')),
    path('orchidlist/', include('orchidlist.urls')),
    path('detail/', include('detail.urls')),
    path('documents/', include('documents.urls')),
    path('donation/', include('donation.urls')),

    # path('sendmail/', include('sendmail.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
