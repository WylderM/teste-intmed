from django.db import models
from .agenda import Agenda

class Consulta(models.Model):
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    horario = models.TimeField()
    data_agendamento = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.agenda} - {self.horario} - {self.data_agendamento}'


    def lista_de_horarios(self):
        return list(Agenda.objects.values_list('horario', flat=True).distinct())

    lista_de_horarios.short_description = 'Horários'


