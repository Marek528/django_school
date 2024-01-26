from django.shortcuts import render
from . models import *

def vypis_blogov(request):
    blogy = Post.objects.all().order_by('publish_date')
    return render(request, 'blog/index.html', {'blogy':blogy})

def vypis_autorov(request):
    autori = Autor.objects.all().order_by('priezvisko')
    return render(request, 'blog/index.html', {'autori':autori})

def vypis_kategorii(request):
    kateogrie = Kategoria.objects.all().order_by('nazov')
    return render(request, 'blog/index.html', {'kategorie':kateogrie})