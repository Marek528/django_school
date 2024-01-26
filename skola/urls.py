from django.contrib import admin
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.vypis_skola, name='skola'),
    path('triedy/', views.vypis_triedy, name='triedy'),
    path('studenti/', views.vypis_student, name='student'),
    path('ucitelia/', views.vypis_ucitelov, name='ucitelov'),
    path("triedy/<trieda>/", views.vypis_trieda, name='trieda'),
]