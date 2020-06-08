from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, User
from bootstrap_datepicker_plus import DatePickerInput
from .models import Clanek, Postava


class ClanekForm(forms.ModelForm):
    class Meta:
        model = Clanek
        fields = ('titulek', 'postava', 'kategorie', 'obsah', 'obrazek',)


class RegistraceForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class PrihlaseniForm(AuthenticationForm):
    class Meta:
        model = User


class PostavaForm(forms.ModelForm):
    class Meta:
        model = Postava
        fields = ('jmeno', 'prijmeni', 'narozeni', 'narodnost', 'vyska', 'nabozenstvi',
                  'politika', 'vzdelani', 'rodice', 'jazyky', 'hobby', 'bio',)
        widgets = {
            'narozeni': DatePickerInput(
                options={
                    "format": "MM/DD/YYYY",
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }),
        }
