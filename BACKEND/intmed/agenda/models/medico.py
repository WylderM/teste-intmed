from django.db import models


# Create your models here.

class Medico(models.Model):
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=200, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.nome

