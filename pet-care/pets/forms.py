from django import forms
from .models import pets

class PetsForm(forms.ModelForm):
    class Meta:
        model = pets
        fields = ['photo', 'name', 'gender_age', 'hair_type', 'origin']