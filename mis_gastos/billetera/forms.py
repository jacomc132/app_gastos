from django import forms
from .models import Billetera

class formulario_crear_billetera(forms.Form):
    nombre_billetera = forms.CharField(max_length=40,label='Nombre billetera')
    total_dinero = forms.IntegerField(label='cantidad dinero',max_value=100000000)


class formulario_crear_ingreso(forms.Form):
    descripcion_ingreso = forms.CharField(max_length = 100, label = "descripción del ingreso")
    valor = forms.FloatField(max_value = 100000000000, label = "valor")




class formulario_crear_gasto(forms.Form):
    descripcion_gasto = forms.CharField(max_length = 100, label = "descripción del gasto")
    valor = forms.FloatField(max_value = 100000000000, label = "valor")




class formulario_crear_categoria(forms.Form):
    nombre_categoria = forms.CharField(max_length = 40, label = "nombre categoria")