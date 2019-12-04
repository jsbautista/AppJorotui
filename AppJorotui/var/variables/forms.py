from django import forms
from .models import Variable

class VariableForm(forms.ModelForm):
    class Meta:
        model = Variable
        fields = [
            'name',
            'tipo',
            'imagen',
            'cantidad',
            'talla',
            'costo',
            'estadoInventario',
        ]
        labels = {
            'name': 'Name',
            'tipo': 'Tipo',
            'imagen' : 'Imagen',
            'cantidad': 'Cantidad',
            'talla' : 'Talla',
            'costo' : 'Costo',
            'estadoInventario': 'EstadoInventario',
        }

