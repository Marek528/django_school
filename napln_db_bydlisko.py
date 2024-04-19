import random
import os
import django
import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from skola.models import *

f = open('ULICE.csv', 'r', encoding='utf8')
lines = f.readlines()

studenti = Student.objects.all()
ucitelia = Ucitel.objects.all()

def get_vek(trieda):
    if trieda[0] == "1":
        return 16
    if trieda[0] == "2":
        return 17
    if trieda[0] == "3":
        return 18
    else:
        return 19

def get_date(vek):
    today = datetime.date.today()
    start_date = datetime.date(today.year - vek, 1, 1)
    end_date = datetime.date(today.year - vek, 12, 31)
    num_days = (end_date - start_date).days
    rand_days = random.randint(1, num_days)
    random_date = start_date + datetime.timedelta(days=rand_days)
    return random_date

for i in studenti:
    random_line = random.choice(lines)
    trieda = i.trieda.nazov
    vek = get_vek(trieda)
    birth = get_date(vek)
    ulica, psc, obec = random_line.split(';')
    i.ulica = f'{ulica} {random.randint(1, 1500)}'
    i.psc = psc
    i.obec = obec
    i.datum_narodenia = birth
    i.save()

for i in ucitelia:
    random_line = random.choice(lines)
    ulica, psc, obec = random_line.split(';')
    i.ulica = f'{ulica} {random.randint(1, 1500)}'
    i.psc = psc
    i.obec = obec
    i.datum_narodenia = birth
    i.save()

