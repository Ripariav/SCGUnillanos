from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from workspace.models import User, Rol
from django.contrib.auth.decorators import user_passes_test
from .forms import AsignarRolForm

# Create your views here.
def user_login(request):
    user = None
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()

    return render(request, 'main/index.html', {'form': form, 'user': user})

def user_logout(request):
    logout(request)
    return redirect('login')

@user_passes_test(lambda u: u.is_staff)
@require_POST
def assign_rol(request):
    form = AsignarRolForm(request.POST)
    if form.is_valid():
        try:
            rol = form.save()
            return JsonResponse({
                'success': True,
                'message': f'Rol {rol.get_rol_display()} asignado correctamente a {rol.usuario.get_full_name()}'
            })
        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': str(e)
            })
    return JsonResponse({
        'success': False,
        'error': 'Datos del formulario inválidos'
    })

@login_required
def profile_view(request):
    # Obtener todos los usuarios excepto el superusuario
    users = User.objects.exclude(is_superuser=True).order_by('first_name')
    
    # Obtener los roles de cada usuario
    for user in users:
        # Usamos roles_list como atributo temporal
        user.roles_list = Rol.objects.filter(usuario=user)

    context = {
        'users': users,
        'form': AsignarRolForm()
    }
    return render(request, 'profile/profile.html', context)







