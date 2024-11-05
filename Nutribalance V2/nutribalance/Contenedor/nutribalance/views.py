
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "index.html")

@login_required
def interfaz(request):
    return render(request, "interfaz.html")
    pass

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registrado exitosamente.')
            return redirect('interfaz')  # Cambia 'home' a la vista principal que desees
        else:
            messages.error(request, 'Hubo un error en el registro.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido, {username}.')
                return redirect('interfaz')  # Cambia 'home' a la vista principal que desees
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('login')  # Cambia 'login' a donde desees redirigir después de cerrar sesión


@login_required
def consulta(request):
    return render(request, "consulta.html")

@login_required
def registro(request):
    return render(request, "registro.html")

@login_required
def mi_perfil(request):
    return render(request, "mi_perfil.html")