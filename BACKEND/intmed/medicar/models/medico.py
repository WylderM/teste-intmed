from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=200, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=200, blank=False, null=False, unique=True)

    def __str__(self):
        return self.nome

    def clean (self):
        if Medico.objects.filter(crm=self.crm).exclude(pk=self.pk).exists():
            raise ValidationError({'crm': ['Este CRM já está em uso.']})

    @staticmethod
    def all_medicos():
        return Medico.objects.all()

    def get_queryset():
        return Medico.objects.all()

