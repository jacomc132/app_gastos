from django.urls import path
from . import views

#Aplicaciones que siguen después de ahorros/
urlpatterns = [
    path("", views.ahorros, name="ahorros"),
    path("crear_ahorro", views.crear_ahorro , name="crear_ahorro"),
    path("<int:id_ahorro>",views.ahorro_actual, name="ahorro_actual"),
    path("<int:id_ahorro>/crear_inversion",views.crear_inversion, name="crear_inversion")
]