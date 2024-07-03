from django import forms
from .models import Suscripciones

class SuscripcionesForm(forms.ModelForm):
    class Meta:
        model = Suscripciones
        fields ='__all__'