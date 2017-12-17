from django import forms
from .models import *


class AlumniForm(forms.ModelForm):
    class Meta:
        model = Alumni
        fields = ['field', 'year', 'typelist', ]
