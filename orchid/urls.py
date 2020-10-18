from django.urls import path
from . import views

# TODO: Add a new page: Compare two species/hybrids
# TODO: Add feature search page - search by color, features
# TODO: Add search by ancestors pair.
# TODO: Add search by location

app_name = 'orchid'
urlpatterns = [
    # Top level
    path('', views.orchid_home, name='orchid_home'),
    # path('newhome', views.new_orchid_home, name='new_orchid_home'),
    # path('oldhome', views.old_orchid_home, name='old_orchid_home'),

    # User accounts
    # path('logout/', views.logout, name='auth_logout'),
    # path('register/', views.signup, name='auth_register'),

    # Documentations
    # path('documents/', views.documents, name='documents'),
    # path('album/', views.album, name='album'),
    # path('project/', views.project, name='project'),
    # path('statistics/', views.statistics, name='statistics'),
    # path('help/', views.help, name='help'),
    # path('newrelease/', views.newrelease, name='newrelease'),
    # path('contact/', views.contact, name='contact'),
    # path('volunteer/', views.volunteer, name='volunteer'),
    # path('submission/', views.submission, name='submission'),

    # Unused high levels
    # path('subfamilies/', views.subfamilies, name='subfamilies'),
    # path('tribes/', views.tribes, name='tribes'),
    # TODO Move id to after acc_species, hyb_species, syn_species, species_detal and hybrid_detail #
    # path('subtribes/', views.subtribes, name='subtribes'),

    # Lists
    path('genera/', views.genera, name='genera'),  # -- All genera
    path('species/', views.all_species, name='species'),  # -- All species
    # path('geodist/', views.geodist, name='geodist'),

    # detail
    path('species_detail/<int:pid>/', views.species, name='species_detail'),
    path('hybrid_detail/<int:pid>/', views.hybrids, name='hybrid_detail'),
    path('<int:pid>/species_detail/', views.species, name='species_detail'),
    path('<int:pid>/hybrid_detail/', views.hybrids, name='hybrid_detail'),
    path('<int:pid>/family_tree/', views.family_tree, name='family_tree'),

    # Support
    path('ancestor/', views.ancestor, name='ancestor'),
    path('progeny/', views.progeny, name='progeny'),
    path('search_match/', views.search_match, name='search_match'),
    # path('search/', views.search, name='search'),

    # path('comment/', views.comment, name='comment'),
    # path('comments/', views.comments, name='comments'),

    path('browse/', views.browse, name='browse'),
    # path('photographers/', views.photographers, name='photographers'),
    # path('foto/(?P<foto>.+)/(?P<type_select>.+)/(?P<pg>[0-9]*)', views.foto, name='foto'),

    # Conventional and fuzzy searches

]
