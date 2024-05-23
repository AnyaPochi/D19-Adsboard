from django_filters import FilterSet, DateFilter
from .models import Respond
from django.forms import SelectDateWidget



class RespondFilter(FilterSet):

    time_in = DateFilter(label='Дата после',
        lookup_expr='gt',
        widget=SelectDateWidget(years=[2023, 2024]))

    class Meta:
        model = Respond
        fields = ['post']





