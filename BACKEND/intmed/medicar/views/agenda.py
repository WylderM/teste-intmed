from rest_framework import viewsets, serializers, generics
from django.utils import timezone
from medicar.models import Agenda,Consulta
from medicar.serializer import AgendaSerializer
from django.shortcuts import get_list_or_404
from django.http import JsonResponse


def lista_agenda (request):
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
            'dia': agenda.dia,
            'horario': agenda.horario,
            'data_agendamento': agenda.data_agenda,
            'medico': medico,
        }
        agenda_list.append(agendamento_dict)
    return JsonResponse(agenda_list, safe=False)




