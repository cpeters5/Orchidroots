from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

def write_output(request, detail=None):
    if str(request.user) != 'chariya' and request.user.is_authenticated:
        message = ">>> " + request.path + str(request.user)
        if detail:
            message += ": " + detail
        logger.warning(message)
        pass

# Create your views here.

def getRole(request):
    role = ''
    if request.user.is_authenticated:
        if 'role' in request.GET:
            role = request.GET['role']
        elif 'role' in request.POST:
            role = request.POST['role']

        if not role:
            if request.user.tier.tier < 2:
                role = 'pub'
            elif request.user.tier.tier == 2:
                role = 'pri'
            else:
                role = 'cur'
        return role
    return role
