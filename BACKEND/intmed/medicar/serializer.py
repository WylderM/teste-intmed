from rest_framework import serializers
from medicar.models import Medico, Agenda, Consulta


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'crm', 'email']

class AgendaSerializer(serializers.ModelSerializer):
   class Meta:
        model = Agenda
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'

class ConsultaListSerializer(serializers.ListSerializer):
    child = ConsultaSerializer()
