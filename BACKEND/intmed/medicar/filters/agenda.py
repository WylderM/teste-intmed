import django_filters

from medicar.models import *


class AgendaFilter(django_filters.FilterSet):
    data_inicio = django_filters.DateFilter(field_name='dia', lookup_expr='gte')
    data_final = django_filters.DateFilter(field_name='dia', lookup_expr='lte')

    class Meta:
        model = Agenda
        fields = ['medico']

