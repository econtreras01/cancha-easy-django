from rest_framework import serializers
from .models import Usuario, Cancha, Reserva, Pago


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ["rut", "nombre", "apellido", "telefono", "email", "es_empleado"]


class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = ["numero", "tipo", "descripcion", "precio_por_hora"]


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ["id_reserva", "usuario", "cancha", "fecha", "hora_inicio", "hora_fin", "estado"]


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ["reserva", "monto", "fecha_pago", "metodo_pago"]
