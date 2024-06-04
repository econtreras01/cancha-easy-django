from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CanchaViewSet, ReservaViewSet, PagoViewSet

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet)
router.register("canchas", CanchaViewSet)
router.register("reservas", ReservaViewSet)
router.register("pagos", PagoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
