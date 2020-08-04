from django.shortcuts import render

# Create your views here.
def list(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/list.html', context)

def bylaws(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/bylaws.html', context)

def articles(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/articles_of_incorporation.html', context)

def req501c3(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/req501c3.html', context)

def disclaimer(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/disclaimer.html', context)

def termsofuse(request):
    context = {'namespace':'termsofuse',}
    return render(request, 'documents/termsofuse.html', context)

def greetings(request):
    context = {'namespace':'greetings',}
    return render(request, 'documents/greetings.html', context)

def identinstruction(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/identinstruction.html', context)

def datamodel(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/datamodel.html', context)


def photosubmissionguideline(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/photoguideline.html', context)

def photoacquisionguideline(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/photoguideline.html', context)


def instructionupload_curate(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/instructionupload_curate.html', context)


def instructionupload_private(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/instructionupload_private.html', context)


def instructionupload_file(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/instructionupload_file.html', context)


def development(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/development.html', context)


def changes(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/R3.html', context)


def termofuse(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/termofuse.html', context)


def privacy_policy(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/privacy_policy.html', context)

def contact(request):
    context = {'namespace':'documents',}
    return render(request, 'documents/contact.html', context)
