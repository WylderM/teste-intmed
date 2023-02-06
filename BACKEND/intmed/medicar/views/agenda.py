from rest_framework import viewsets, serializers, generics
from django.utils import timezone
from medicar.models import Agenda,Consulta
from medicar.serializer import AgendaSerializer
from django.shortcuts import get_list_or_404
from django.http import JsonResponse

from datetime import date

from medicar.filter import *
from medicar.serializers import *

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.filter(dia__gte=date.today(), horario__isnull=False).order_by('dia')
    serializer_class = AgendaSerializer
    filter_class = AgendaFilter



