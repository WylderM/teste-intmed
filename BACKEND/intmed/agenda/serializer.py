from rest_framework import serializers
from agenda.models import Medico

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'name', 'crm', 'email']
