from rest_framework import serializers
from medicar.models import *

class ConsultaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Consulta
        fields = ['id', 'agenda', 'horario', 'data_agendamento', 'medico']
        read_only_fields = ['data_agendamento', 'medico']
