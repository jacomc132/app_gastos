from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Billetera, Ingreso, Gasto, Categoria
from ahorros.models import Ahorro,Inversion
from .forms import formulario_crear_billetera,formulario_crear_ingreso_gasto,formulario_crear_categoria
from django.utils import timezone



'''
*Página principal de app billetera.
*Realiza consulta a base de datos para mostrar en pantalla todas las billeteras por medio del templare billeteras.html
'''
def billetera(request):
    mis_billeteras = Billetera.objects.all()
    return render(request,'billetera.html',{'mis_billeteras':mis_billeteras})

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
        ahorro_seleccionado=request.POST['ahorro_id']
        nueva_billetera = Billetera(nombre_billetera = request.POST['nombre_billetera'], fecha_creacion=fecha_actual, total_dinero = request.POST['total_dinero'],ahorro_id=Ahorro.objects.get(pk=ahorro_seleccionado))
        nueva_billetera.save()
        ahorro = Ahorro.objects.get(pk=ahorro_seleccionado)
        ahorro.cantidad_dinero = ahorro.cantidad_dinero + float(request.POST['total_dinero'])
        ahorro.save()
        return redirect('/billetera')


'''
*Vista que recibe como parámetros un request, id de billetera del ingreso.
*Realiza una consulta a base de datos para mostrar información de la billetera actual mediante el template billetera_actual.html
'''
def billetera_actual(request,ruta_billetera):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    return render(request,'billetera_actual.html',
    {
        'nombre_billetera':billetera.nombre_billetera,
        'billetera_pk':billetera.pk,
        'billetera':billetera
        })


'''
*Vista que recibe como parámetros un request, id de billetera del ingreso.
*Realiza consultas en bases de datos con ese id y por último renderiza el template gastos.html
'''
def ingresos_gastos(request,ruta_billetera,categoria_type):
    billetera = Billetera.objects.get(pk = ruta_billetera)
    categorias = Categoria.objects.filter(tipo_categoria=categoria_type)
    categorias = categorias.filter(billetera_id=ruta_billetera)
    return render(request,'ingresos_gastos.html',
    {
        'nombre_billetera': billetera.nombre_billetera,
        'billetera':billetera,
        'categorias':categorias,
        'tipo_categoria':categoria_type
    })



'''
View que permite crear una categoría, la categoría pertenecerá a ingresos ó gastos, esto 
depende del parámetro dado por la url.
'''
def crear_categoria(request,ruta_billetera,categoria_type):
    if request.method == 'GET':
        billetera = Billetera.objects.get(pk=ruta_billetera)
        return render(request,"crear_categoria.html",{'formulario_crear_categoria':formulario_crear_categoria,
        'tipo_categoria':categoria_type,
        'billetera':billetera
        })
    
    elif request.method == 'POST':
        billetera = Billetera.objects.get(pk = ruta_billetera)
        billetera.categoria_set.create(billetera_id=ruta_billetera,nombre_categoria=request.POST['nombre_categoria'],tipo_categoria=categoria_type)
        return redirect(f'/billetera/{ruta_billetera}/{categoria_type}')

'''

'''
def categoria_actual(request,ruta_billetera,categoria_type,categoria_id):
    mi_billetera = Billetera.objects.get(pk = ruta_billetera)
    categoria = Categoria.objects.get(pk = categoria_id)
    tipo_categoria = categoria_type
    
    if categoria_type == 'ingresos':
        ingresos = Ingreso.objects.filter(categoria_id = categoria_id)
        ingresos = ingresos.filter(billetera_id=ruta_billetera)
        return render(request,"categoria_actual.html",
        {
            'billetera': mi_billetera,
            'categoria':categoria,
            'tipo_categoria':tipo_categoria,
            'ingresos_o_gastos':ingresos
            })

    elif categoria_type == 'gastos':
        gastos = Gasto.objects.filter(categoria_id = categoria_id)
        gastos = gastos.filter(billetera_id=ruta_billetera)
        return render(request,"categoria_actual.html",
        {
            'billetera': mi_billetera,
            'categoria':categoria,
            'tipo_categoria':tipo_categoria,
            'ingresos_o_gastos':gastos
            })

'''

'''
def crear_ingreso_gasto(request,ruta_billetera,categoria_type,categoria_id):
    billetera = Billetera.objects.get(pk=ruta_billetera)
    ahorro_asociado = Ahorro.objects.get(pk=billetera.ahorro_id.pk)

    if request.method == 'GET':
        categoria = Categoria.objects.get(pk=categoria_id)
        return render(request,"crear_ingreso_gasto.html",{'formulario_crear_ingreso_gasto':formulario_crear_ingreso_gasto,'categoria':categoria})

    elif request.method == 'POST':
        billetera = Billetera.objects.get(pk=ruta_billetera)
        categoria = Categoria.objects.get(pk=categoria_id)

        if categoria_type == 'ingresos':
            billetera.ingreso_set.create(billetera_id=billetera.pk,categoria_id=categoria,descripcion=request.POST['descripcion'],valor=request.POST['valor'])
            billetera.total_dinero = billetera.total_dinero + float(request.POST['valor'])
            billetera.save()
            ahorro_asociado.cantidad_dinero = ahorro_asociado.cantidad_dinero + float(request.POST['valor'])
            ahorro_asociado.save()
            return redirect(f'/billetera/{ruta_billetera}/{categoria_type}/{categoria_id}')

        elif categoria_type == 'gastos':
            billetera.gasto_set.create(billetera_id=billetera.pk,categoria_id=categoria,descripcion=request.POST['descripcion'],valor=request.POST['valor'])
            billetera.total_dinero = billetera.total_dinero - float(request.POST['valor'])
            billetera.save()
            ahorro_asociado.cantidad_dinero = ahorro_asociado.cantidad_dinero - float(request.POST['valor'])
            ahorro_asociado.save()
            return redirect(f'/billetera/{ruta_billetera}/{categoria_type}/{categoria_id}')

    

def eliminar_billetera(request,ruta_billetera):
    billetera=Billetera.objects.get(pk=ruta_billetera)
    billetera.delete()
    return redirect(f"/billetera")




def eliminar_categoria(request,ruta_billetera,categoria_type,categoria_id):
    categoria=Categoria.objects.get(pk=categoria_id)
    billetera = Billetera.objects.get(pk=ruta_billetera)
    ahorro = Ahorro.objects.get(pk=billetera.ahorro_id.pk)

    if categoria_type == "ingresos":
        ingresos = Ingreso.objects.filter(categoria_id=categoria_id)
        for ingreso in ingresos:
            billetera.total_dinero = float(billetera.total_dinero) - float(ingreso.valor)
            billetera.save()
            ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) - float(ingreso.valor)
            ahorro.save()

    elif categoria_type == "gastos":
        gastos = Gasto.objects.filter(categoria_id=categoria_id)
        for gasto in gastos:
            billetera.total_dinero = float(billetera.total_dinero) + float(gasto.valor)
            billetera.save()
            ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) + float(gasto.valor)
            ahorro.save()

    categoria.delete()
    return redirect(f"/billetera/{ruta_billetera}/{categoria_type}")




def eliminar_ingreso_gasto(request,ruta_billetera,categoria_type,categoria_id,ingreso_gasto_id):
    billetera = Billetera.objects.get(pk=ruta_billetera)
    ahorro = Ahorro.objects.get(pk=billetera.ahorro_id.pk)
    if categoria_type == "ingresos":
        ingreso = Ingreso.objects.get(pk=ingreso_gasto_id)
        billetera.total_dinero = float(billetera.total_dinero) - float(ingreso.valor)
        billetera.save()
        ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) - float(ingreso.valor)
        ahorro.save()
        ingreso.delete()
        return redirect(f"/billetera/{ruta_billetera}/{categoria_type}/{categoria_id}")
    
    elif categoria_type == "gastos":
        gasto = Gasto.objects.get(pk=ingreso_gasto_id)
        billetera.total_dinero = float(billetera.total_dinero) + float(gasto.valor)
        billetera.save()
        ahorro.cantidad_dinero = float(ahorro.cantidad_dinero) + float(gasto.valor) 
        ahorro.save()
        gasto.delete()
        return redirect(f"/billetera/{ruta_billetera}/{categoria_type}/{categoria_id}")
    













