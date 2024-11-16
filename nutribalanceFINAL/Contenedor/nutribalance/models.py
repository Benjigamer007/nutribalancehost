from django.db import models
from django.contrib.auth.hashers import make_password


class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    edad = models.PositiveIntegerField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Peso en kg
    altura = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)  # Altura en cm
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otro', 'Otro')], null=True, blank=True)
    

    def save(self, *args, **kwargs):
        # Cifrar la contraseña antes de guardarla
        if not self.pk:  # Solo cifra si es un nuevo registro
            self.password = make_password(self.password)
        super(Paciente, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"



    

