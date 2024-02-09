from django.shortcuts import render, HttpResponse
from . models import *

def calc(request):
    if (request.method == "GET"):
        return render(request, 'calc/index.html')
    else:
        try:
            a = float(request.POST["a"])
            b = float(request.POST["b"])
        except:
            vysledok = "Zadaj cisla!"
            return render(request, 'calc/index.html', {"vysledok":vysledok})
        operator = request.POST["operator"]

        if (operator == '+'):
            vysledok = a + b
        if (operator == '-'):
            vysledok = a - b
        if (operator == '*'):
            vysledok = a * b
        if (operator == '/'):
            if (b == 0):
                vysledok = "Nulou sa delit neda"
                return render(request, 'calc/index.html', {"vysledok":vysledok})
            else:
                vysledok = a / b

        try:
            priklad_check = Priklady.objects.get(a=a, b=b, operator=operator)
        except:
            priklad = Priklady(
                a = a,
                b = b,
                operator = operator,
                vysledok = vysledok
            )
            priklad.save()

        return render(request, 'calc/index.html', {"a":a, "b":b, 'operator':operator, "vysledok":vysledok})