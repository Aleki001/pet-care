from django import forms
from .models import Pets, AdoptionRequest

class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = ['photo', 'name', 'gender_age', 'hair_type', 'origin']


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }