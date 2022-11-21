from django.urls import path
from . import views

#Aplicaciones que siguen después de billetera/
urlpatterns = [
    path("", views.billetera, name="billetera"),
    path("crear_billetera",views.crear_billetera, name = "crear_billetera"),
    path("<int:ruta_billetera>",views.billetera_actual, name = "billetera_actual"),
    path("<int:ruta_billetera>/gastos",views.gastos, name = "gastos"),
    path("<int:ruta_billetera>/ingresos",views.ingresos, name = "ingresos")
]
