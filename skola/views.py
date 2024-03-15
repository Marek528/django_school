from django.shortcuts import render, HttpResponse
from . models import *

def vypis_skola(request):
    triedy = Trieda.objects.all().order_by("nazov")
    studenti = Student.objects.all().order_by("priezvisko")
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, 'skola/index.html', {"triedy":triedy, "ucitelia":ucitelia, "studenti":studenti})

def vypis_triedy(request):
    triedy = Trieda.objects.all().order_by("nazov")
    return render(request, 'skola/index.html', {"triedy":triedy})

def vypis_student(request):
    studenti = Student.objects.all().order_by("priezvisko")
    return render(request, 'skola/index.html', {"studenti":studenti})

def vypis_ucitelov(request):
    ucitelia = Ucitel.objects.all().order_by("priezvisko")
    return render(request, 'skola/index.html', {"ucitelia":ucitelia})

def vypis_trieda(request, trieda):
    id_trieda = Trieda.objects.get(nazov=trieda).pk
    studenti = Student.objects.filter(trieda_id=id_trieda).order_by("priezvisko")
    studenti_list = []
    for student in studenti:
        studenti_list.append(f"{student.meno} {student.priezvisko}")
    ucitel = Ucitel.objects.get(trieda_id=id_trieda)
    ucitel = f"{ucitel.titul} {ucitel.meno} {ucitel.priezvisko}"
    # return HttpResponse(f"{trieda} <br> {ucitel} <br> {studenti_list} ")
    return render(request, 'skola/trieda_list.html', {"trieda":trieda, "ucitel":ucitel, "studenti":studenti_list})

def student_detail(request, student):
    student = Student.objects.get(id=student)
    trieda = Trieda.objects.get(nazov=student.trieda)
    triedny_ucitel = Ucitel.objects.get(trieda=trieda.id)
    return render(request, 'skola/student_detail.html', {'student': student, 'trieda': trieda, 'triedny_ucitel': triedny_ucitel})

def ucitel_detail(request, ucitel):
    ucitel = Ucitel.objects.get(id=ucitel)
    if ucitel.trieda:
        trieda = Trieda.objects.get(nazov=ucitel.trieda)
    trieda = 'nie je triedny ucitel'
    return render(request, 'skola/ucitel_detail.html', {'ucitel': ucitel, 'trieda': trieda})