from django.shortcuts import render, redirect
from .models import Contrato
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SuperUserCreationForm, ContratoForm

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
def homeview(request):
    
    return render(request, 'main/home.html')

@login_required
def contractview(request):
    contratos = Contrato.objects.all()
    return render(request, 'main/contract.html',{'contratos': contratos})

@login_required
def profileview(request):
    return render(request, 'main/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST['full_name'].split()[0]
        user.last_name = " ".join(request.POST['full_name'].split()[1:])
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect('profile')
    
    return render(request, 'main/edit_profile.html')

@login_required
def create_contractview(request):
    contratos = Contrato.objects.all()
    return render(request, 'main/create_contract.html', {'contratos': contratos})

@login_required
def crear_contrato(request):
    if request.method == 'POST':
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'El contrato ha sido creado con éxito.')
            return redirect('crear_contrato')  # Redirige a la misma página o a donde desees
        else:
            messages.error(request, 'Hubo un error al crear el contrato. Verifica los campos.')
    else:
        form = ContratoForm()
    
    return render(request, 'main/create_contract.html', {'form': form})


def create_superuser(request):
    if request.method == 'POST':
        form = SuperUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Superuser created successfully.')
            return redirect('create_superuser')  # Cambia la redirección si lo necesitas
    else:
        form = SuperUserCreationForm()
    
    return render(request, 'main/superuser.html', {'form': form})
