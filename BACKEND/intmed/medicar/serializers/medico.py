from rest_framework import serializers
from medicar.models import *

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico

        fields = ['id', 'nome', 'crm', 'email']
