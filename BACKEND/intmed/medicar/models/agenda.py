from django.db import models
from .medico import Medico
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Agenda(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    dia = models.DateField(max_length=200, blank=False, null=False)
    horario = ArrayField(models.TimeField(), null=True)

    class Meta:
        unique_together = (('medico', 'dia'),)

    def __str__(self):
        return f'{self.dia} {self.horario} {self.medico.nome}'

    def clean(self):
        if Agenda.objects.filter(medico=self.medico, dia=self.dia).exclude(pk=self.pk).exists():
            raise ValidationError({'medico': ['Já existe uma agenda para este médico neste dia.']})
        if self.dia < timezone.now().date():
            raise ValidationError({'dia': ['Não é possível criar uma agenda para um dia passado.']})




