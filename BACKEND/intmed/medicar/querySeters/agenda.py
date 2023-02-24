from medicar.models import Agenda
from datetime import date

class AgendaQuerySet:

    @staticmethod
    def get_agendas_by_day():
        return Agenda.objects.filter(dia__gte=date.today(), horario__isnull=False).order_by('dia')
