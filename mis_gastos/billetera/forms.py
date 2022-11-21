from django import forms

class formulario_crear_billetera(forms.Form):
    nombre_billetera = forms.CharField(max_length=40,label='Nombre billetera')
    total_dinero = forms.IntegerField(label='cantidad dinero',max_value=10000)

