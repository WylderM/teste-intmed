from django.db import models

# Create your models here.

class Agendamento(models.Model):
    medico = models.CharField(max_length=200, blank=False, null=False)
    dia = models.DateField(blank=False, null=False)
    horario = models.TimeField(max_length=200, blank=False, null=False)


    def __str__(self):
        return self.medico

