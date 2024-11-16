from django import forms
from .models import Paciente


class PacienteForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Paciente
        fields = ['nombre', 'apellido', 'email', 'password']

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class DatosPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['edad', 'peso', 'altura', 'sexo']
        
        
