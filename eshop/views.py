from django.shortcuts import render
from . models import *

def vypis_kategorii(request):
    category = Category.objects.all().order_by('nazov')
    return render(request, 'eshop/index.html', {"category":category})

def vypis_eshopu(request):
    produkty = Product.objects.all().order_by('nazov')
    category = Category.objects.all().order_by('nazov')
    return render(request, 'eshop/index.html', {'produkty':produkty, 'category':category})

def vypis_objednavok(request):
    objednavky = Objednavka.objects.all().order_by('datum')
    return render(request, 'eshop/index.html', {'objednavky':objednavky})

def vypis_zakaznikov(request):
    zakaznici = Zakaznik.objects.all().order_by('priezvisko')
    return render(request, 'eshop/index.html', {'zakaznici':zakaznici})

def vypis_kategoria(request, kategoria):
    id_kategoria = Category.objects.get(nazov=kategoria).pk
    produkty = Product.objects.filter(kategoria_id=id_kategoria).order_by('nazov')
    produkty_list = []
    for produkt in produkty:
        produkty_list.append(produkt)
    return render(request, 'eshop/produkty_list.html', {"kategoria":kategoria, "produkty":produkty})

def popis_produktu(request, produkt):
    produkty = Product.objects.filter(id=produkt).order_by('nazov')
    return render(request, 'eshop/popis_produktu.html', {'produkty':produkty})
