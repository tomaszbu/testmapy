from django import forms
from django.core import validators


class FormName(forms.Form): # tutaj mamy formularz bez modelu dlatego dziedziczymy bez ModelForm
    #tworzymy pola formularza
    # trzeba doczytać w dokumentacji jakie są możliwości tworzenia pól typu charfield itd...
    lat = forms.FloatField()
    lng = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea)
