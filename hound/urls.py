from django.urls import path
from .views import GuiaViewSet

guia_list = GuiaViewSet.as_view({"get": "list"})
guia_create = GuiaViewSet.as_view({"post": "create"})
guia_update = GuiaViewSet.as_view({"put": "update"})
guia_get = GuiaViewSet.as_view({"get": "retrieve"})
guia_delete = GuiaViewSet.as_view({"delete": "destroy"})

urlpatterns = [
    path("guias", guia_list, name="guias"),
    path("crear-guia", guia_create, name="crear-guia"),
    path("actualizar-guia/<int:pk>", guia_update, name="actualizar-guia"),
    path("obtener-guia/<int:pk>", guia_get, name="obtener-guia"),
    path("eliminar-guia/<int:pk>", guia_delete, name="eliminar-guia"),
]