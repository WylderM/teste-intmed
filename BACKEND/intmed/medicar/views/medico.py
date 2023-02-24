from rest_framework import viewsets, generics
from medicar.models import Medico
from medicar.serializers import *
from medicar.querySeters.medico import MedicoQuerySet

class MedicoViewSet(viewsets.ModelViewSet):
    serializer_class = MedicoSerializer

    def get_queryset(self):
        return MedicoQuerySet.get_all_medicos()

