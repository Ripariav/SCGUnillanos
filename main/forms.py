# main/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from workspace.models import Rol

class AsignarRolForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=User.objects.exclude(is_superuser=True).order_by('first_name'),
        label="Usuario",
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
        empty_label="Seleccione un usuario"
    )
    rol = forms.ChoiceField(
        choices=Rol.USUARIO_ROLES,
        label="Rol",
        widget=forms.Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = Rol
        fields = ['usuario', 'rol']

    def clean(self):
        cleaned_data = super().clean()
        usuario = cleaned_data.get('usuario')
        rol = cleaned_data.get('rol')

        # Verificar si ya existe un rol para este usuario
        if Rol.objects.filter(usuario=usuario, rol=rol).exists():
            raise forms.ValidationError("Este usuario ya tiene asignado este rol.")
        
        return cleaned_data
