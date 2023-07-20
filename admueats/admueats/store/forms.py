from django.forms import ModelForm
from .models import Occupancy 

class Occupancy(ModelForm):
    class Meta:
        model=Occupancy,
        fields=('____all___',)