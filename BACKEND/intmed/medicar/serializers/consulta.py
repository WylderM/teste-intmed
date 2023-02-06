from rest_framework import serializers
from medicar.models import *

class ConsultaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Consulta
        fields = ['id', 'agenda', 'horario', 'data_agendamento']
        read_only_fields = ['data_agendamento']

class CreateConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'horario']
        read_only_fields = ['data_agendamento']
