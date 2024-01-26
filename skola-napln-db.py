import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *

Trieda.objects.all().delete()
Ucitel.objects.all().delete()
Student.objects.all().delete()

triedy = []
for i in range(1, 5):
    for trieda in ["A", "B", "C", "D"]:
        triedy.append(f'{i}.{trieda}')
        Trieda.objects.create(nazov=f'{i}.{trieda}')
    
fmena = open('mena.txt', 'r', encoding='utf-8')
mena = fmena.read().splitlines()

fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
priezviska = fpriezviska.read().splitlines()

for i in range(20):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    titul = random.choice(["Mgr.", "Ing.", "PhDr.", "PaeDr.", ""])
    if i < len(triedy):
        trieda = Trieda.objects.get(nazov=triedy[i])
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko, trieda=trieda)
    else:
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)

for i in range(100):
    meno = random.choice(mena)
    priezvisko = random.choice(priezviska)
    trieda = Trieda.objects.get(nazov=random.choice(triedy))
    Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=trieda)