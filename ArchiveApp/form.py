from django import forms
from .models import Movies

class Posters(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ["img"]  