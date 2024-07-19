from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, CanchaViewSet, ReservaViewSet, PagoViewSet, login_view

router = DefaultRouter()
router.register("usuarios", UsuarioViewSet)
router.register("canchas", CanchaViewSet)
router.register("reservas", ReservaViewSet)
router.register("pagos", PagoViewSet)

urlpatterns = [path("login/", login_view, name="login"), path("", include(router.urls))]
