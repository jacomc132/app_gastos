from django.test import TestCase
from django.utils import timezone
from .models import Ingreso,Billetera,Categoria
from ahorros.models import Ahorro

class TestIngresoModelsTests(TestCase):
    """An income cant be a negative number"""
    def test_ingreso_es_negativo(self):
        ahorro = Ahorro.objects.create(nombre_ahorro="Ahorro jaco",fecha_creacion=timezone.now(),cantidad_dinero = 1000)
        billetera = Billetera.objects.create(nombre_billetera="billetera",fecha_creacion=timezone.now(),total_dinero=1000,ahorro_id=ahorro)
        categoria = Categoria.objects.create(billetera_id = billetera,nombre_categoria = "gastos en general",tipo_categoria="ingresos")
        ingreso = Ingreso(billetera_id =billetera,categoria_id=categoria,descripcion="ingreso1",valor=-12)
        self.assertIs(ingreso.positivo(),True)