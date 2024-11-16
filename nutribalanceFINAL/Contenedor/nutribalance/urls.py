from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página de inicio
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # Ruta para el escaneo de puertos
    path('inicio/', views.inicio, name='inicio'),
    path('mi_perfil/', views.mi_perfil, name='miperfil'),
    path('registro/', views.registro, name='registro'),
    path('consulta/', views.consulta, name='consulta'),
    path('contact', views.contact, name='contact'),
    path('registro_exitoso/', views.registro_exitoso, name='registro_exitoso'),
    path('datos_paciente/', views.datos_paciente_view, name='datos_paciente'),
    path('editar-perfil/<int:id>/', views.editar_perfil, name='editar_perfil'),
    
]