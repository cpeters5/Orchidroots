# -*- coding: utf8 -*-
from django.http import HttpResponseRedirect
from django.apps import apps
Genus = apps.get_model('orchiddb', 'Genus')
Species = apps.get_model('orchiddb', 'Species')

def acc_species(request, pid):
    genus = Genus.objects.get(pk=pid)
    send_url = '/orchidlist/species/?type=species&genus=' + str(genus.genus)
    # print(send_url)
    return HttpResponseRedirect(send_url)

def hyb_species(request, pid):
    genus = Genus.objects.get(pk=pid)
    send_url = '/orchidlist/species/?type=hybrid&tab=sum&genus=' + str(genus.genus)
    # print(send_url)
    return HttpResponseRedirect(send_url)


def species(request, pid):
    try:
        species = Species.objects.get(pk=pid)
    except Species.DoesNotExist:
        return HttpResponseRedirect('/')

    send_url = '/detail/information/' + str(species.pid) + "/"
    # print(send_url)
    return HttpResponseRedirect(send_url)


def family_tree (request,pid):
    gen = ''
    if 'gen' in request.GET:
        gen = request.GET['gen']

    send_url = '/detail/ancestor/' + str(pid) + '/?gen=gen&tab=anc&role=pub&state=show'
    return HttpResponseRedirect(send_url)

def browse(request):
    send_url = '/orchidlist/browse/?display=selected'
    return HttpResponseRedirect(send_url)
