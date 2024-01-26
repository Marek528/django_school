from django.contrib import admin
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.vypis_blogov, name='vypis-blogov'),
    path('autori/', views.vypis_autorov, name='vypis-autorov'),
    path('kategorie/', views.vypis_kategorii, name='vypis-kategorii')
]
