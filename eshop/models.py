from django.db import models
from django.utils import timezone

class Category(models.Model):
    nazov = models.CharField(max_length=35)

    def __str__(self):
        return f'{self.nazov}'

class Product(models.Model):
    nazov = models.CharField(max_length=50)
    kategoria = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    cena = models.DecimalField(max_digits=6, decimal_places=2)
    popis = models.TextField()

    def __str__(self):
        return f'{self.nazov}, {self.kategoria}, {self.cena}, {self.popis}'

class Zakaznik(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    email = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.meno} {self.priezvisko}, {self.email}'

class Objednavka(models.Model):
    zakaznik = models.ForeignKey(Zakaznik, on_delete=models.SET_NULL, null=True, blank=True)
    tovar = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    datum = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return f'{self.zakaznik}, {self.tovar}, {self.datum}'

