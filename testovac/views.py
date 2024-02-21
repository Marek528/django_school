from django.shortcuts import render
from calc.models import *

def testovac(request):
    global nahodny_priklad

    if (request.method == "GET"):
        nahodny_priklad = Priklady.objects.order_by('?').first()
        return render(request, 'testovac/index.html', {"a":nahodny_priklad.a, "b":nahodny_priklad.b, 'operator':nahodny_priklad.operator})
    else:
        vysledok = float(request.POST["vysledok"])
        if (vysledok == nahodny_priklad.vysledok):
            kontrola = "Spravne!"
        else:
            kontrola = "Nespravne!"

        nahodny_priklad = Priklady.objects.order_by('?').first()
        return render(request, 'testovac/index.html',
        {"a":nahodny_priklad.a, "b":nahodny_priklad.b, 'operator':nahodny_priklad.operator, "kontrola":kontrola, 'vysledok':vysledok})