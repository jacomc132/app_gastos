from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Billetera, Ingreso, Gasto
from .forms import formulario_crear_billetera, formulario_crear_ingreso, formulario_crear_gasto
from django.utils import timezone



'''
*Página principal de app billetera.
*Realiza consulta a base de datos para mostrar en pantalla todas las billeteras por medio del templare billeteras.html
'''
def billetera(request):
    mis_billeteras = Billetera.objects.all()
    return render(request,'billetera.html',{'mis_billeteras':mis_billeteras})


'''
*Vista que recibe como parámetros un request, id de billetera del ingreso.
*Realiza una consulta a base de datos para mostrar información de la billetera actual mediante el template billetera_actual.html
'''
def billetera_actual(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    return render(request,'billetera_actual.html',
    {
        'nombre_billetera':billetera.nombre_billetera,
        'billetera_pk':billetera.pk
        })


'''
*Vista que recibe como parámetros un request, id de billetera del ingreso.
*Realiza consultas en bases de datos con ese id y por último renderiza el template gastos.html
'''
def gastos(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    gastos_billetera = Gasto.objects.filter(billetera_id = ruta_billetera)
    return render(request,'gastos.html',
    {
        'nombre_billetera': billetera.nombre_billetera,
        'gastos_billetera':gastos_billetera,
        'billetera':billetera
    })


'''
*Vista que recibe como parámetros un request, id de billetera del ingreso.
*Realiza consultas en bases de datos con ese id y por último renderiza el template ingresos.html
'''
def ingresos(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    ingresos_billetera = Ingreso.objects.filter(billetera_id = ruta_billetera)
    return render(request,'ingresos.html',
    {
        'nombre_billetera': billetera.nombre_billetera,
        'ingresos_billetera':ingresos_billetera,
        'billetera':billetera
    })


'''
*Vista que recibe como parámetros un request.
*Permite crear una nueva billetera por medio de una interfaz de usuario.
'''
def crear_billetera(request):
    if request.method == 'GET':
        #Mostrar interfaz
        return render(request,"crear_billetera.html",{'form':formulario_crear_billetera})
    elif request.method == 'POST':
        #Método POST (Postear info en base de datos)
        fecha_actual = timezone.now()
        nueva_billetera = Billetera(nombre_billetera = request.POST['nombre_billetera'], fecha_creacion=fecha_actual, total_dinero = request.POST['total_dinero'])
        nueva_billetera.save()
        return redirect('/billetera')

'''
Vista que recibe la ruta de la billetera (billetera_id) y permite crearle un ingreso.
'''
def crear_ingreso(request,ruta_billetera):
    if request.method == 'GET':
        return render(request,"crear_ingreso.html",{'formulario_crear_ingreso':formulario_crear_ingreso})

    elif request.method == 'POST':
        billetera_actual = Billetera.objects.get(pk=ruta_billetera)
        billetera_actual.ingreso_set.create(descripcion_ingreso=request.POST['descripcion_ingreso'],valor=request.POST['valor'])
        return redirect(f'/billetera/{ruta_billetera}/ingresos')



'''
Vista que recibe la ruta de la billetera (billetera_id) y permite crearle un gasto.
'''
def crear_gasto(request,ruta_billetera):
    if request.method == 'GET':
        return render(request,"crear_gasto.html",{'formulario_crear_gasto':formulario_crear_gasto})


    elif request.method == 'POST':
        billetera_actual = Billetera.objects.get(pk = ruta_billetera)
        billetera_actual.gasto_set.create(descripcion_gasto=request.POST['descripcion_gasto'],valor=request.POST['valor'])
        return redirect(f'/billetera/{ruta_billetera}/gastos')