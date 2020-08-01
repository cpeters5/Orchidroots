# from django.conf.urls import url, include
from django.urls import path
from . import views

# TODO: Add a new page: Compare two species/hybrids
# TODO: Add feature search page - search by color, features
# TODO: Add search by ancestors pair.
# TODO: Add search by location

app_name = 'orchidlist'
urlpatterns = [
    # Lists
    path('family/', views.family, name='family'),  # -- All species
    path('subfamily/', views.subfamily, name='subfamily'),  # -- All species
    path('tribe/', views.tribe, name='tribe'),  # -- All species
    path('subtribe/', views.subtribe, name='subtribe'),  # -- All species
    path('genera/', views.genera, name='genera'),  # -- All species
    path('species/', views.species_list, name='species'),  # -- All species
    path('hybrid/', views.hybrid_list, name='hybrid'),  # -- All species
    path('progeny/<int:pid>/', views.progeny, name='progeny'),
    path('progenyimg/<int:pid>/', views.progenyimg, name='progenyimg'),
    path('subgenus/', views.subgenus, name='subgenus'),  # -- All species
    path('section/', views.section, name='section'),  # -- All species
    path('subsection/', views.subsection, name='subsection'),  # -- All species
    path('series/', views.series, name='series'),  # -- All species

    path('browsegen/', views.browsegen, name='browsegen'),
    path('browse/', views.browse, name='browse'),
    path('browsedist/', views.browsedist, name='browsedist'),

    # Legacy urls
]
