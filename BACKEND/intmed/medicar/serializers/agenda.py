from rest_framework import serializers
from medicar.models import *

class AgendaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Agenda
        fields = ['id', 'dia', 'medico', 'horario']
