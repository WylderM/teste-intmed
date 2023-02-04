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
    # # agenda = Agenda.objects.filter(horario = 'horario')

    # # print("AQUI: ", horarios_display)
    # # def horarios_display(self, agenda):
    # #     return ', '.join(Agenda.objects.filter(horario = 'horario').all().values_list('horario', flat=True))

    # # horarios_display.short_description = 'Horários'

    list_display = ('agenda', 'realizada')
    search_fields = ('agenda', 'realizada')
admin.site.register(Consulta, Consultas)
