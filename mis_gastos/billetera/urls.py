from django.urls import path
from . import views

#Aplicaciones que siguen después de billetera/
urlpatterns = [
    path("", views.billetera, name="billetera"),
    path("crear_billetera",views.crear_billetera, name = "crear_billetera"),
    path("<int:ruta_billetera>",views.billetera_actual, name = "billetera_actual"),
    path("<int:ruta_billetera>/<str:categoria_type>",views.ingresos_gastos, name = "ingresos_gastos"),
    path("<int:ruta_billetera>/<str:categoria_type>/crear_categoria",views.crear_categoria, name="crear_categoria"),
    path("<int:ruta_billetera>/<str:categoria_type>/<int:categoria_id>",views.categoria_actual, name = "categoria_actual"),
    path("<int:ruta_billetera>/<str:categoria_type>/<int:categoria_id>/crear_ingreso_gasto",views.crear_ingreso_gasto, name="crear_ingreso_gasto"),
    path("eliminar_billetera/<int:ruta_billetera>",views.eliminar_billetera,name="eliminar_billetera"),
    path("<int:ruta_billetera>/<str:categoria_type>/<int:categoria_id>/eliminar_categoria",views.eliminar_categoria, name="eliminar_categoria"),
    path("<int:ruta_billetera>/<str:categoria_type>/<int:categoria_id>/<int:ingreso_gasto_id>/eliminar_ingreso_gasto",views.eliminar_ingreso_gasto, name="eliminar_ingreso_gasto")
]