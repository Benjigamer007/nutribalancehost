
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import PacienteForm, LoginForm, DatosPacienteForm
from .models import Paciente
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from .decorators import paciente_login_required
from .forms import DatosPacienteForm
from django.shortcuts import render, get_object_or_404


def home(request):
    return render(request, "home.html")

def inicio(request):
    return render(request, "inicio.html")


def register_view(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save()  # Guarda el nuevo paciente en la base de datos

            # Guarda el ID del paciente en la sesión para autenticar
            request.session['paciente_id'] = paciente.id
            messages.success(request, f'Bienvenido, {paciente.nombre}!')

            # Redirige a la vista de datos del paciente
            return redirect('datos_paciente')  
    else:
        form = PacienteForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                paciente = Paciente.objects.get(email=email)
                if check_password(password, paciente.password):
                    # Guarda el ID del paciente en la sesión para indicar que está autenticado
                    request.session['paciente_id'] = paciente.id
                    messages.success(request, f'Bienvenido, {paciente.nombre}.')
                    return redirect('home')  # Redirige a la página de inicio
                else:
                    messages.error(request, 'Contraseña incorrecta.')
            except Paciente.DoesNotExist:
                messages.error(request, 'El correo electrónico no está registrado.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    request.session.flush()  # Limpia toda la sesión
    messages.info(request, 'Has cerrado sesión.')
    return redirect('login')


@paciente_login_required
def consulta(request):
    return render(request, "consulta.html")


def registro(request):
    return render(request, "registro.html")


#def mi_perfil(request):
    return render(request, "mi_perfil.html")


def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('email-template.html', {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        })

        emailSender = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            # ACA VA EL CORREO O LA LISTA DE CORREOS A LOS QUE QUIERO ENVIAR ESTE EMAIL. PUEDE SER UNO O TANTOS COMO LOS QUE DESEE
            # SI ES UNO SOLO, COLOCO EL CORREO UNICO ENTRE COMILLAS SIMPLES Y NADA MAS. SI AGREGO MÁS TENGO QUE SEPARARLOS CON UNA COMA ','
            ['lauti10oporto@gmail.com']
        )
        emailSender.content_subtype = 'html'
        emailSender.fail_silently = False
        emailSender.send()

        return redirect('consulta')

def registro_exitoso(request):
    return render(request, 'registro_exitoso.html')

def datospaciente(request):
    return render(request, 'datospaciente.html')

def datos_paciente_view(request):
    paciente = Paciente.objects.get(id=request.session['paciente_id'])  # Obtiene el paciente logueado

    if request.method == 'POST':
        form = DatosPacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()  # Guarda los datos adicionales en el perfil del paciente
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('home')  # Redirige a la página de inicio
    else:
        form = DatosPacienteForm(instance=paciente)

    return render(request, 'datospaciente.html', {'form': form, 'nombre': paciente.nombre})

def mi_perfil(request):
    paciente_id = request.session.get('paciente_id')
    if not paciente_id:
        # Si no hay paciente_id en la sesión, redirige al login
        messages.error(request, "No has iniciado sesión.")
        return redirect('login')

    try:
        # Intenta obtener el paciente de la base de datos
        paciente = Paciente.objects.get(id=paciente_id)
    except Paciente.DoesNotExist:
        messages.error(request, "No se encontró el paciente en la base de datos.")
        return redirect('login')

    return render(request, 'mi_perfil.html', {'paciente': paciente})

def editar_perfil(request, id):
    paciente = get_object_or_404(Paciente, id=id)  # Obtiene el paciente por ID

    if request.method == 'POST':
        form = DatosPacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('miperfil')  # Redirige a la página de perfil después de guardar
    else:
        form = DatosPacienteForm(instance=paciente)

    return render(request, 'editar_perfil.html', {'form': form, 'paciente': paciente})