from django.shortcuts import render
from datetime import datetime, timedelta
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.apps import apps
import random
import string

Genus       = apps.get_model('orchiddb', 'Genus')
Species     = apps.get_model('orchiddb', 'Species')
SpcImages     = apps.get_model('orchiddb', 'SpcImages')
HybImages     = apps.get_model('orchiddb', 'HybImages')
Comment     = apps.get_model('orchiddb', 'Comment')

def orchid_home(request):
    randgenus = Genus.objects.exclude(status='synonym').extra(where=["num_spc_with_image + num_hyb_with_image > 0"]).values_list('pid',flat=True).order_by('?')
    print("randgenus = ",len(randgenus))
    # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 0)
    # request.session['num_visits'] = num_visits + 1

    randimages = []
    for e in randgenus:
        if len(randimages) > 11:
            break
        if SpcImages.objects.filter(gen=e):
            randimages.append(SpcImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=9).order_by('?')[0:1][0])

    random.shuffle(randimages)
    role = ''
    if 'role' in request.GET:
        role = request.GET['role']

    context = {'title': 'orchid_home', 'role':role,
               # 'num_visits':num_visits,
               'randimages':randimages,
               'level':'detail','tab':'sum','namespace':'myproject',}
    return render(request, 'orchid_home.html', context)


@login_required
def private_home(request):
    # Home page after private users login

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    genus_list = Genus.objects.all()

    context = {'num_visits':num_visits,
               'title': 'private_home', 'level':'home','namespace':'myproject',}
    return render(request, 'node.html', context)


def home(request):
    num_img = 4
    # Exclude genus ignorta
    genus_list = Genus.objects.exclude(status='synonym').filter(pid__lt=999999999)
    rangenusspc_list = genus_list.filter(num_spc_with_image__gt=0).values_list('pid',flat=True).order_by('?')[0:num_img]
    rangenushyb_list = genus_list.filter(num_hyb_with_image__gt=0).values_list('pid',flat=True).order_by('?')[0:num_img]

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
            randimagesspc.append(SpcImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=9).order_by('?')[0:1][0])
    for e in rangenushyb_list:
        if len(randimageshyb) > num_img:
            break
        if HybImages.objects.filter(gen=e):
            randimageshyb.append(HybImages.objects.filter(gen=e).filter(rank__gt=0).filter(rank__lt=9).order_by('?')[0:1][0])

    genus_list = Genus.objects.exclude(status='synonym').filter(Q(num_species__gte=0) | Q(num_hybrid__gte=0))
    context = {'title': 'orchid_home', 'num_visits':num_visits,
               'randimagesspc':randimagesspc,'randimageshyb':randimageshyb,'genus_list':genus_list,
               'level':'detail','tab':'sum','namespace':'myproject',}
    return render(request, 'orchid_home.html', context)


