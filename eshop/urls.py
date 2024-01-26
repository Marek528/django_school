from django.contrib import admin
from django.urls import path, include
from .  import views

urlpatterns = [
    path('', views.vypis_eshopu, name='vypis-eshopu'),
    path('kategorie/', views.vypis_kategorii, name='vypis-kategorii'),
    path('objednavky/', views.vypis_objednavok, name='vypis-objednavok'),
    path('zakaznici/', views.vypis_zakaznikov, name='vypis-zakaznici'),
]
