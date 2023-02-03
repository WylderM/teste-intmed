from django.contrib import admin

# Register your models here.
from agenda.models import Medico
from agenda.models import Agendamento


class Medicos(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email')
    search_fields = ('nome', 'crm', 'email')
admin.site.register(Medico, Medicos)

class Agendamentos(admin.ModelAdmin):
    list_display = ('medico', 'dia', 'horario')
    search_fields = ('medico', 'dia', 'horario')

admin.site.register(Agendamento, Agendamentos)
