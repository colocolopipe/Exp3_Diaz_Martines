from django import forms


class SuscripcionesForm(forms.ModelForm):
    class Meta:
        model = Suscripciones
        fields ='__all__'

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields ='__all__'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
