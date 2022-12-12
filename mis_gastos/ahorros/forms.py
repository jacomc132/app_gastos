from django import forms
from .models import Ahorro,Inversion

class formulario_crear_ahorro(forms.Form):
    nombre_ahorro = forms.CharField(max_length=40, label="Nombre ahorro")
    cantidad_dinero = forms.FloatField(label="Cantidad dinero")




class formulario_crear_inversion(forms.Form):
    CHOICES = (("1","Activo"),("2","Pasivo"))
    nombre_inversion = forms.CharField(max_length=60, label="Nombre inversión")
    ahorro_id = forms.ModelChoiceField(Ahorro.objects.all(), label="Ahorro asociado")
    tipo_inversion = forms.ChoiceField(widget=forms.Select, choices=CHOICES, label="Tipo de inversión")
    valor_inversion = forms.FloatField(label="Valor inversión")

