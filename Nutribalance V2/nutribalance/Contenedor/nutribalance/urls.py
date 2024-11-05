from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Ruta para la página de inicio
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'), # Ruta para el escaneo de puertos
    path('interfaz/', views.interfaz, name='interfaz'),
    path('miperfil/', views.mi_perfil, name='miperfil'),
    path('registro/', views.registro, name='registro'),
    path('consulta/', views.consulta, name='consulta'),
]