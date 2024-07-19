from rest_framework import viewsets
from .models import Usuario, Cancha, Reserva, Pago
from .serializers import (
    UsuarioSerializer,
    CanchaSerializer,
    ReservaSerializer,
    PagoSerializer,
)
from urllib import request as urllib_request, error as urllib_error
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
import json
import requests


@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data.get("email")
        password = data.get("password")

        # Verifica el email y la contraseña en la base de datos
        response = requests.get("http://127.0.0.1:8000/api/usuarios/")
        usuarios = response.json()

        for usuario in usuarios:
            if usuario["email"] == email and usuario["password"] == password:
                return JsonResponse({"message": "Inicio de sesión exitoso", "es_empleado": usuario.get("es_empleado", False)}, status=200)  # Incluye el campo `es_empleado` en la respuesta

        return JsonResponse({"message": "Credenciales incorrectas"}, status=401)

    return JsonResponse({"message": "Método no permitido"}, status=405)


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class CanchaViewSet(viewsets.ModelViewSet):
    queryset = Cancha.objects.all()
    serializer_class = CanchaSerializer


class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer
