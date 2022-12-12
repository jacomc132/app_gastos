from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import formulario_crear_ahorro, formulario_crear_inversion
from .models import Ahorro,Inversion
from django.utils import timezone
from billetera.models import Billetera,Ingreso, Gasto

# Create your views here.
def ahorros(request):
    ahorros=Ahorro.objects.all()
    return render(request,'ahorros.html',{'ahorros':ahorros})



def crear_ahorro(request):
    if request.method == 'GET':
        return render(request,'crear_ahorro.html',{'formulario_crear_ahorro':formulario_crear_ahorro})


    elif request.method == 'POST':
        fecha_actual=timezone.now()
        nuevo_ahorro = Ahorro(nombre_ahorro=request.POST['nombre_ahorro'],fecha_creacion=fecha_actual,cantidad_dinero=request.POST['cantidad_dinero'])
        nuevo_ahorro.save()
        return redirect('/ahorros')



def ahorro_actual(request,id_ahorro):
    ahorro = Ahorro.objects.get(pk=id_ahorro)
    billeteras_ahorro = Billetera.objects.filter(ahorro_id=id_ahorro)
    return render(request,'ahorro_actual.html',{'ahorro':ahorro,'billeteras_ahorro':billeteras_ahorro})



def crear_inversion(request,id_ahorro):
    
    if request.method == 'GET':
        return render(request,'crear_inversion.html',{'formulario_crear_inversion':formulario_crear_inversion})
    
    elif request.method == 'POST':
        return redirect(f'/ahorros/{id_ahorro}')