from django.contrib import admin

# Register your models here.
from medicar.models import Medico, Agenda, Consulta

class Medicos(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email')
    search_fields = ('nome', 'crm', 'email')
admin.site.register(Medico, Medicos)

class Agendas(admin.ModelAdmin):
    list_display = ('medico', 'dia', 'horario')
    search_fields = ('medico', 'dia', 'horario')
admin.site.register(Agenda, Agendas)

class Consultas(admin.ModelAdmin):
    list_display = ('agenda', 'horario', 'data_agendamento')
    search_fields = ('agenda', 'horario', 'data_agendamento')
admin.site.register(Consulta, Consultas)
