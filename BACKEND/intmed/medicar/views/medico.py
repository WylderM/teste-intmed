from rest_framework import viewsets, generics
from medicar.models import Medico
from medicar.serializers import *

class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

