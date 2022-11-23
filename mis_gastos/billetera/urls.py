from django.urls import path
from . import views

#Aplicaciones que siguen después de billetera/
urlpatterns = [
    path("", views.billetera, name="billetera"),
    path("crear_billetera",views.crear_billetera, name = "crear_billetera"),
    path("<int:ruta_billetera>",views.billetera_actual, name = "billetera_actual"),
    path("<int:ruta_billetera>/crear_categoria",views.crear_categoria, name="crear_categoria"),
    path("<int:ruta_billetera>/<int:ruta_categoria>",views.categoria_actual, name = "categoria_actual"),
    path("<int:ruta_billetera>/<int:ruta_categoria>/gastos",views.gastos, name = "gastos"),
    path("<int:ruta_billetera>/<int:ruta_categoria>/ingresos",views.ingresos, name = "ingresos"),
    path("<int:ruta_billetera>/<int:ruta_categoria>/ingresos/crear_ingreso",views.crear_ingreso, name="crear_ingreso"),
    path("<int:ruta_billetera>/<int:ruta_categoria>/gastos/crear_gasto",views.crear_gasto, name="crear_gasto")
]
