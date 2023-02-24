from medicar.models import Consulta

class ConsultaQuerySet:

    @staticmethod
    def get_all_consultas():
        return Consulta.objects.all()
