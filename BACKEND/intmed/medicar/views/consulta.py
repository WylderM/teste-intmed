from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from medicar.models import Agenda, Consulta
from rest_framework import viewsets
from rest_framework.response import Response
from medicar.serializers import *
from datetime import datetime
from rest_framework.response import Response
from rest_framework import status
from medicar.querySeters.consulta import ConsultaQuerySet
class ConsultaViewSet(viewsets.ModelViewSet):
    serializer_class = ConsultaSerializer


    def get_queryset(self):
        return ConsultaQuerySet.get_all_consultas()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        agenda = Agenda.objects.get(pk=request.data.get('agenda_id'))
        horario = request.data.get('horario')

        # Verificar se horário está disponível na agenda
        consulta_existente = Consulta.objects.filter(agenda=agenda, horario=horario).exists()
        if consulta_existente:
            return Response({'message': 'Horário não disponível'}, status=status.HTTP_400_BAD_REQUEST)

        # Verificar se horário é passado
        if agenda.dia < datetime.date.today() or (agenda.dia == datetime.date.today() and horario < datetime.datetime.now().time()):
            return Response({'message': 'Não é possível agendar para um dia e horário passados'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list (self, request, *args, **kwargs):
        consultas = get_list_or_404(Consulta)
        agendas = get_list_or_404(Agenda)
        consulta_list = []
        for consulta in consultas:
            for agenda in agendas:
                medico = {
                    'id': agenda.medico.id,
                    'crm': agenda.medico.crm,
                    'nome': agenda.medico.nome,
                    'email': agenda.medico.email,
                }
            agendamento_dict = {
                'id': consulta.id,
                'dia': agenda.dia,
                'horario': consulta.horario,
                'data_agendamento': consulta.data_agendamento,
                'medico': medico,
            }
            consulta_list.append(agendamento_dict)
        return JsonResponse(consulta_list, safe=False)





