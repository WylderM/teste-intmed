from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from medicar.models import Agenda, Consulta
from rest_framework import viewsets, generics
from rest_framework.response import Response
from django.utils import timezone
from medicar.serializer import ConsultaSerializer


def lista_consulta(request):
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


