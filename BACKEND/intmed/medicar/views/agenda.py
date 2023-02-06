from rest_framework import viewsets
from medicar.models import Agenda
from medicar.serializers import *
from django.shortcuts import get_list_or_404
from django.http import JsonResponse
from datetime import date
from medicar.filter import *
from medicar.serializers import *

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.filter(dia__gte=date.today(), horario__isnull=False).order_by('dia')
    serializer_class = AgendaSerializer
    filter_class = AgendaFilter

    def list (self, request, *args, **kwargs):
        agendas = get_list_or_404(Agenda)
        agenda_list = []
        for agenda in agendas:
            medico = {
                'id': agenda.medico.id,
                'crm': agenda.medico.crm,
                'nome': agenda.medico.nome,
                'email': agenda.medico.email,
            }
            agendamento_dict = {
                'id': agenda.id,
                'medico': medico,
                'dia': agenda.dia,
                'horario': agenda.horario,

            }
            agenda_list.append(agendamento_dict)
        return JsonResponse(agenda_list, safe=False)





