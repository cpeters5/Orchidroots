from django.urls import path
from . import views

# Documentations

app_name = 'documents'
urlpatterns = [
    # path('about/', views.about, name='about'),
    path('list/', views.list, name='list'),
    path('articles/', views.articles, name='articles'),
    path('req501c3/', views.req501c3, name='req501c3'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('termsofuse/', views.termsofuse, name='termsofuse'),
    path('greetings/', views.greetings, name='greetings'),
    # path('assets/$', views.assets, name='assets'),
    path('bylaws/', views.bylaws, name='bylaws'),
    path('identinstruction/', views.identinstruction, name='identinstruction'),
    path('photosubmissionguideline/', views.photosubmissionguideline, name='photosubmissionguideline'),
    path('photoacquisionguideline/', views.photoacquisionguideline, name='photoacquisionguideline'),
    path('instructionupload_curate/', views.instructionupload_curate, name='instructionupload_curate'),
    path('instructionupload_private/', views.instructionupload_private, name='instructionupload_private'),
    path('instructionupload_file/', views.instructionupload_file, name='instructionupload_file'),
    path('development/', views.development, name='development'),
    path('datamodel/', views.datamodel, name='datamodel'),
    path('changes/', views.changes, name='changes'),
    # path('contact/', views.contact, name='contact'),
    # path('copyright/', views.copyright, name='copyright'),
    # path('FAQ/', views.FAQ, name='FAQ'),
    # path('help/', views.help, name='help'),
    # path('newrelease/', views.newrelease, name='newrelease'),
    # path('personnel/', views.personnel, name='personnel'),
    # path('project/', views.project, name='project'),
    # path('statistics/', views.statistics, name='statistics'),
    # path('submission/', views.photo_submission, name='submission'),
    # path('terms/', views.terms_of_use, name='terms'),
    # path('rvolunteer/', views.volunteer, name='volunteer'),
]
