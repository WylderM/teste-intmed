from medicar.models import Medico

class MedicoQuerySet:

    @staticmethod
    def get_all_medicos():
        return Medico.objects.all()
