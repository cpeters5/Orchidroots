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
