from django import forms
from .models import Billetera

class formulario_crear_billetera(forms.Form):
    nombre_billetera = forms.CharField(max_length=40,label='Nombre billetera', widget=forms.TextInput(attrs={'class':'input1'}))
    total_dinero = forms.IntegerField(label='cantidad dinero',max_value=100000000, widget=forms.TextInput(attrs={'class':'input2'}))


class formulario_crear_ingreso_gasto(forms.Form):
    descripcion = forms.CharField(max_length = 100, label = "descripción")
    valor = forms.FloatField(max_value = 100000000000, label = "valor")


class formulario_crear_categoria(forms.Form):
    nombre_categoria = forms.CharField(max_length = 40, label = "nombre categoria")