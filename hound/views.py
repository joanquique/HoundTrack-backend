from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Guia
from .serializers import GuiaSerializer


class GuiaViewSet(viewsets.ViewSet):
    """
    Endpoints requeridos:
      - POST   api/crear-guia
      - PUT    api/actualizar-guia/<id>
      - GET    api/obtener-guia/<id>
      - DELETE api/eliminar-guia/<id>
    """

    def create(self, request):
        serializer = GuiaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        guia = serializer.save()
        return Response(GuiaSerializer(guia).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            guia = Guia.objects.get(pk=pk)
        except Guia.DoesNotExist:
            return Response({"detail": "Guía no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        return Response(GuiaSerializer(guia).data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        try:
            guia = Guia.objects.get(pk=pk)
        except Guia.DoesNotExist:
            return Response({"detail": "Guía no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GuiaSerializer(guia, data=request.data)  # PUT
        serializer.is_valid(raise_exception=True)
        guia = serializer.save()
        return Response(GuiaSerializer(guia).data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            guia = Guia.objects.get(pk=pk)
        except Guia.DoesNotExist:
            return Response({"detail": "Guía no encontrada."}, status=status.HTTP_404_NOT_FOUND)

        guia.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)