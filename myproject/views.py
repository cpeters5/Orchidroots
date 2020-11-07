from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.apps import apps
import random
import string

Genus = apps.get_model('orchiddb', 'Genus')
Species = apps.get_model('orchiddb', 'Species')
SpcImages = apps.get_model('orchiddb', 'SpcImages')
HybImages = apps.get_model('orchiddb', 'HybImages')
Comment = apps.get_model('orchiddb', 'Comment')
num_img = 20


def orchid_home(request):
    randgenus = Genus.objects.exclude(status='synonym').extra(where=["num_spc_with_image + num_hyb_with_image > 0"]
                                                              ).values_list('pid', flat=True).order_by('?')
    # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    randimages = []
    for e in randgenus:
        if len(randimages) >= num_img:
            break
        if SpcImages.objects.filter(gen=e):
            randimages.append(SpcImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=7
                                                                    ).order_by('-rank','quality','?')[0:1][0])

    random.shuffle(randimages)
    role = 'pub'
    if 'role' in request.GET:
        role = request.GET['role']

    context = {'title': 'orchid_home', 'role': role, 'randimages': randimages, 'level': 'detail', 'tab': 'sum', }
    return render(request, 'orchid_home.html', context)


@login_required
def private_home(request):
    # Home page after private users login
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'num_visits': num_visits, 'title': 'private_home', 'level': 'home', }
    return render(request, 'node.html', context)


# Portal - in progressw
def home(request):
    # Exclude genus ignorta
    genus_list = Genus.objects.exclude(status='synonym').filter(pid__lt=999999999)
    rangenusspc_list = genus_list.filter(num_spc_with_image__gt=0).values_list('pid', flat=True
                                                                               ).order_by('?')[0: num_img]
    rangenushyb_list = genus_list.filter(num_hyb_with_image__gt=0).values_list('pid', flat=True
                                                                               ).order_by('?')[0: num_img]

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Generate random images
    randimagesspc = []
    randimageshyb = []
    for e in rangenusspc_list:
        if len(randimagesspc) > num_img:
            break
        if SpcImages.objects.filter(gen=e):
            randimagesspc.append(SpcImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=9
                                                                                           ).order_by('?')[0: 1][0])
    for e in rangenushyb_list:
        if len(randimageshyb) > num_img:
            break
        if HybImages.objects.filter(gen=e):
            randimageshyb.append(HybImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=9
                                                                                           ).order_by('?')[0: 1][0])

    genus_list = Genus.objects.exclude(status='synonym').filter(Q(num_species__gte=0) | Q(num_hybrid__gte=0))
    context = {'title': 'orchid_home', 'num_visits': num_visits,
               'randimagesspc': randimagesspc, 'randimageshyb': randimageshyb, 'genus_list': genus_list,
               'level': 'detail', 'tab': 'sum', }
    return render(request, 'home.html', context)


def require_get(view_func):
    def wrap(request, *args, **kwargs):
        if request.method != "GET":
            return HttpResponseBadRequest("Expecting GET request")
        return view_func(request, *args, **kwargs)
    wrap.__doc__ = view_func.__doc__
    wrap.__dict__ = view_func.__dict__
    wrap.__name__ = view_func.__name__
    return wrap


@require_get
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
