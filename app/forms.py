from django import forms
from .models import Suscripciones, Persona

class SuscripcionesForm(forms.ModelForm):
    class Meta:
        model = Suscripciones
        fields ='__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields ='__all__'
