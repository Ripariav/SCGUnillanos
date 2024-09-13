# main/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contrato

class SuperUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.is_superuser = True
        user.is_staff = True
        if commit:
            user.save()
        return user

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['codigo_unspsc', 'dependencia_responsable', 'descripcion', 'observaciones', 'fecha_estimada_inicio', 'fecha_estimada_ofertas']