from django.db import models
from .agenda import Agenda

class Consulta(models.Model):
    agenda = models.OneToOneField(Agenda, on_delete=models.CASCADE)
    realizada = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.agenda} - {self.realizada}'


    def lista_de_horarios(self):
        return list(Agenda.objects.values_list('horario', flat=True).distinct())

    lista_de_horarios.short_description = 'Horários'


