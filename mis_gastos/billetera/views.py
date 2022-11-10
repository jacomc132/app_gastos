from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Billetera, Ingreso, Gasto


def billetera(request):
    mis_billeteras = Billetera.objects.all()
    return render(request,'billetera.html',{'mis_billeteras':mis_billeteras})


def billetera_actual(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    return render(request,'billetera_actual.html',
    {
        'nombre_billetera':billetera.nombre_billetera,
        'billetera_pk':billetera.pk
        })


def gastos(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    gastos_billetera = Gasto.objects.filter(billetera_id = ruta_billetera)
    return render(request,'gastos.html',
    {
        'nombre_billetera': billetera.nombre_billetera,
        'gastos_billetera':gastos_billetera
    })


def ingresos(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    ingresos_billetera = Ingreso.objects.filter(billetera_id = ruta_billetera)
    return render(request,'ingresos.html',
    {
        'nombre_billetera': billetera.nombre_billetera,
        'ingresos_billetera':ingresos_billetera
    })
