from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from .forms import formulario_crear_ahorro, formulario_crear_inversion
from .models import Ahorro,Inversion
from django.utils import timezone
from billetera.models import Billetera,Ingreso, Gasto
from datetime import date
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/home/login')
def ahorros(request):
    ahorros=Ahorro.objects.all()
    return render(request,'ahorros.html',{'ahorros':ahorros})


@login_required(login_url='/home/login')
def crear_ahorro(request):
    if request.method == 'GET':
        return render(request,'crear_ahorro.html',{'formulario_crear_ahorro':formulario_crear_ahorro})


    elif request.method == 'POST':
        fecha_actual=timezone.now()
        nuevo_ahorro = Ahorro(nombre_ahorro=request.POST['nombre_ahorro'],fecha_creacion=fecha_actual,cantidad_dinero=request.POST['cantidad_dinero'])
        nuevo_ahorro.save()
        return redirect(reverse('ahorros:ahorros'))



@login_required(login_url='/home/login')
def ahorro_actual(request,id_ahorro):
    ahorro = Ahorro.objects.get(pk=id_ahorro)
    billeteras_ahorro = Billetera.objects.filter(ahorro_id=id_ahorro)
    inversiones_ahorro = Inversion.objects.filter(ahorro_id=id_ahorro)
    return render(request,'ahorro_actual.html',{'ahorro':ahorro,'billeteras_ahorro':billeteras_ahorro,'inversiones_ahorro':inversiones_ahorro})



@login_required(login_url='/home/login')
def crear_inversion(request,id_ahorro):
    if request.method == 'GET':
        return render(request,'crear_inversion.html',{'formulario_crear_inversion':formulario_crear_inversion})
    
    elif request.method == 'POST':
        ahorro_seleccionado = Ahorro.objects.get(pk=id_ahorro)
        nueva_inversion = Inversion(nombre_inversion=request.POST['nombre_inversion'],ahorro_id= ahorro_seleccionado,tipo_inversion=request.POST['tipo_inversion'],valor_inversion=request.POST['valor_inversion'],fecha_creacion=timezone.now(),ROI=request.POST["ROI"])
        nueva_inversion.save()
        ahorro_seleccionado.cantidad_dinero = ahorro_seleccionado.cantidad_dinero - float(nueva_inversion.valor_inversion)
        ahorro_seleccionado.save()
        return redirect(f'/ahorros/{id_ahorro}')



@login_required(login_url='/home/login')
def eliminar_ahorro(request,id_ahorro):
    ahorro = Ahorro.objects.get(pk = id_ahorro)
    ahorro.delete()
    return redirect(f'/ahorros')
    


@login_required(login_url='/home/login')
def modificar_ahorro(request,id_ahorro):
    ahorro = Ahorro.objects.get(pk=id_ahorro)

    if request.method == "GET":
        return render(request,'modificar_ahorro.html',{'ahorro':ahorro})


    elif request.method=="POST":
        ahorro.nombre_ahorro = request.POST['nombre_ahorro']
        ahorro.cantidad_dinero = request.POST['cantidad_dinero']
        ahorro.save()
        return redirect(f"/ahorros")
    

@login_required(login_url='/home/login')
def eliminar_inversion(request,id_ahorro,id_inversion):
    ahorro = Ahorro.objects.get(pk=id_ahorro)
    inversion=Inversion.objects.get(pk=id_inversion)
    ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) + float(inversion.valor_inversion)
    ahorro.save()
    inversion.delete()
    return redirect(f'/ahorros/{id_ahorro}')



@login_required(login_url='/home/login')
def modificar_inversion(request,id_ahorro,id_inversion):
    ahorro = Ahorro.objects.get(pk=id_ahorro)
    inversion = Inversion.objects.get(pk=id_inversion)

    if request.method == 'GET':
        return render(request,'modificar_inversion.html',{'ahorro':ahorro,'inversion':inversion})

    elif request.method == 'POST':
        ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) + float(inversion.valor_inversion)
        ahorro.save()
        inversion.nombre_inversion = request.POST["nombre_inversion"]
        inversion.tipo_inversion = request.POST['tipo_inversion']
        inversion.valor_inversion = request.POST['valor_inversion']
        inversion.ROI = request.POST['ROI']
        ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) - float(inversion.valor_inversion)
        ahorro.save()
        inversion.save()
        return redirect(f"/ahorros/{ahorro.pk}")











