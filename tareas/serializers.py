from django.utils import timezone
from rest_framework import serializers
from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    dias_desde_creacion = serializers.SerializerMethodField(read_only=True)
    estado_display = serializers.ReadOnlyField(source='get_estado_display')

    class Meta:
        model = Tarea
        fields = [
            'id', 'titulo', 'descripcion', 'estado', 'estado_display',
            'prioridad', 'created', 'updated', 'dias_desde_creacion',
        ]
        read_only_fields = ['id', 'created', 'updated']

    def get_dias_desde_creacion(self, obj):
        return (timezone.now() - obj.created).days

    def validate_titulo(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El título debe tener al menos 3 caracteres."
            )
        return value.strip()

    def validate(self, data):
        estado = data.get('estado', getattr(self.instance, 'estado', None))
        descripcion = data.get('descripcion', getattr(self.instance, 'descripcion', ''))
        if estado == 'completada' and not descripcion:
            raise serializers.ValidationError(
                "Una tarea completada debe tener una descripción."
            )
        return data