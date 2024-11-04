from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from workspace.models import User, Rol
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def user_login(request):
    user = None
    
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

@login_required
@require_POST
@user_passes_test(lambda u: u.is_staff)
def assign_rol(request):
    user_id = request.POST.get('user')
    rol_name = request.POST.get('rol')
    
    try:
        user = User.objects.get(id=user_id)
        rol, created = Rol.objects.get_or_create(user=user, defaults={'rol': rol_name})
        if not created:
            rol.rol = rol_name
            rol.save()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
def profile_view(request):
    context = {}
    if request.user.is_staff:
        context['users'] = User.objects.all()
    return render(request, 'profile/profile.html', context)





