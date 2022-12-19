from django.db import models

# Create your models here.

class Ahorro(models.Model):
    nombre_ahorro = models.CharField(max_length = 40)
    fecha_creacion = models.DateTimeField("date published")
    cantidad_dinero = models.FloatField(default = 0)


    def __str__(self):
        return self.nombre_ahorro
    




class Inversion(models.Model):
    nombre_inversion = models.CharField(max_length=60)
    ahorro_id = models.ForeignKey(Ahorro, on_delete=models.CASCADE)
    tipo_inversion = models.CharField(max_length = 50)
    valor_inversion = models.FloatField(default=0)

    def __str__(self):
        return self.nombre_inversion





