from rest_framework import serializers
from .models import Guia


class GuiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guia
        fields = [
            "id",
            "trackingNumber",
            "origin",
            "destination",
            "currentStatus",
            "createdAt",
            "updatedAt",
        ]
        read_only_fields = ["id", "createdAt", "updatedAt"]