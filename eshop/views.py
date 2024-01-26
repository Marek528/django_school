from django.shortcuts import render
from . models import *

def vypis_kategorii(request):
    category = Category.objects.all().order_by('nazov')
    return render(request, 'eshop/index.html', {"category":category})

def vypis_eshopu(request):
    produkty = Product.objects.all().order_by('nazov')
    return render(request, 'eshop/index.html', {'produkty':produkty})

def vypis_objednavok(request):
    objednavky = Objednavka.objects.all().order_by('datum')
    return render(request, 'eshop/index.html', {'objednavky':objednavky})

def vypis_zakaznikov(request):
    zakaznici = Zakaznik.objects.all().order_by('priezvisko')
    return render(request, 'eshop/index.html', {'zakaznici':zakaznici})