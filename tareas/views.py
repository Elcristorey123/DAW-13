from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

    filterset_fields = ['estado', 'prioridad']
    search_fields = ['titulo', 'descripcion']
    ordering_fields = ['created', 'prioridad', 'titulo']
    ordering = ['-created']

    @action(detail=False, methods=['get'])
    def completadas(self, request):
        tareas = self.get_queryset().filter(estado='completada')
        page = self.paginate_queryset(tareas)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(tareas, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def completar(self, request, pk=None):
        tarea = self.get_object()
        tarea.estado = 'completada'
        tarea.save()
        serializer = self.get_serializer(tarea)
        return Response(serializer.data)