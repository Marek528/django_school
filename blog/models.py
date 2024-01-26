from django.db import models
from django.utils import timezone

class Autor(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    username = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username}, {self.meno} {self.priezvisko}'

class Kategoria(models.Model):
    nazov = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.nazov}'

class Post(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    nazov = models.CharField(max_length=100)
    publish_date = models.DateTimeField(default = timezone.now)
    create_date = models.DateTimeField(default = timezone.now)
    text = models.TextField()
    kategoria = models.ForeignKey(Kategoria, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f'{self.autor}, {self.nazov}, {self.publish_date}, {self.create_date}, {self.text}, {self.kategoria}'