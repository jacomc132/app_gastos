from django import forms
from .models import Ahorro,Inversion

class formulario_crear_ahorro(forms.Form):
    nombre_ahorro = forms.CharField(max_length=40, label="Nombre ahorro")
    cantidad_dinero = forms.FloatField(label="Cantidad dinero")




class formulario_crear_inversion(forms.Form):
    CHOICES = (("Activo","Activo"),("Pasivo","Pasivo"))
    nombre_inversion = forms.CharField(max_length=60, label="Nombre inversión")
    tipo_inversion = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label="Tipo de inversión")
    valor_inversion = forms.FloatField(label="Valor inversión")

