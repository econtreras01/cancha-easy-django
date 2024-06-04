from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    rut = models.CharField(max_length=10, unique=True, primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    es_empleado = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["rut", "nombre", "apellido", "email", "telefono"]

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
