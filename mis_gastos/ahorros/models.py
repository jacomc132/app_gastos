from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
'''usuario por defecto: jacomc132'''
usuario = User.objects.get(username = 'jacomc132')

class Ahorro(models.Model):
    nombre_ahorro = models.CharField(max_length = 40)
    fecha_creacion = models.DateTimeField("date published")
    cantidad_dinero = models.FloatField(default = 0)
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE,default=usuario.pk)

    def __str__(self):
        return self.nombre_ahorro
    




class Inversion(models.Model):
    nombre_inversion = models.CharField(max_length=60)
    ahorro_id = models.ForeignKey(Ahorro, on_delete=models.CASCADE)
    tipo_inversion = models.CharField(max_length = 50)
    valor_inversion = models.FloatField(default=0)
    fecha_creacion = models.DateTimeField(default=timezone.now())
    ROI = models.IntegerField(default=0)
    usuario_id = models.ForeignKey(User,on_delete=models.CASCADE,default=usuario.pk)

    def __str__(self):
        return self.nombre_inversion





