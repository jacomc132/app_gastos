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
]