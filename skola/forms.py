from django import forms
from . models import Uzivatel

class UzivatelForm(forms.ModelForm):
    
    class Meta:
        model = Uzivatel
        fields = "__all__"