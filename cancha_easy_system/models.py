import uuid
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


class Cancha(models.Model):
    deporte = [
        (1, "Fútbol"),
        (2, "Tenis"),
        (3, "Vóleibol"),
    ]
    numero = models.IntegerField(primary_key=True)
    tipo = models.IntegerField(choices=deporte)
    descripcion = models.TextField(blank=True)
    precio_por_hora = models.IntegerField()

    def __str__(self):
        return f"Cancha de {dict(self.deporte)[self.tipo]} N° {self.numero}"


class Reserva(models.Model):
    ESTADO_RESERVA = [
        (1, "Por pagar"),
        (2, "Pagada"),
        (3, "Cancelada"),
    ]
    id_reserva = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    estado = models.IntegerField(choices=ESTADO_RESERVA, default=1)
    arriendo_balon = models.BooleanField(default=False, null=True)
    luz_artificial = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f"{self.usuario.username} - Cancha {self.cancha.numero} - {self.fecha} {self.hora_inicio}-{self.hora_fin}"


class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    monto = models.IntegerField()
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=50)

    def __str__(self):
        return f"Pago de {self.monto} por {self.reserva}"
