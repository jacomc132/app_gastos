from django.urls import path
from . import views

#Aplicaciones que siguen después de ahorros/
urlpatterns = [
    path("", views.ahorros, name="ahorros"),
    path("crear_ahorro", views.crear_ahorro , name="crear_ahorro"),
    path("<int:id_ahorro>",views.ahorro_actual, name="ahorro_actual"),
    path("<int:id_ahorro>/crear_inversion",views.crear_inversion, name="crear_inversion"),
    path("<int:id_ahorro>/eliminar_ahorro",views.eliminar_ahorro, name="eliminar_ahorro"),
    path("<int:id_ahorro>/modificar_ahorro",views.modificar_ahorro, name="modificar_ahorro"),
    path("<int:id_ahorro>/<int:id_inversion>/eliminar_inversion",views.eliminar_inversion,name="eliminar_inversion"),
    path("<int:id_ahorro>/<int:id_inversion>/modificar_inversion",views.modificar_inversion,name="modificar_inversion"),
]