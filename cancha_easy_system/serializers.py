from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario, Cancha, Reserva, Pago


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = (["rut", "nombre", "apellido", "telefono", "email", "es_empleado"],)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class CanchaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancha
        fields = ["numero", "tipo", "descripcion", "precio_por_hora"]


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = [
            "id_reserva",
            "usuario",
            "cancha",
            "fecha",
            "hora_inicio",
            "hora_fin",
            "estado",
        ]


class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = ["reserva", "monto", "fecha_pago", "metodo_pago"]
