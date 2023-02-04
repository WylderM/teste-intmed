from rest_framework import viewsets, generics
from medicar.models import Medico
from medicar.serializer import MedicoSerializer

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

