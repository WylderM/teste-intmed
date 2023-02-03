from rest_framework import viewsets
from agenda.models import Medico
from agenda.serializer import MedicoSerializer

class MedicosViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
