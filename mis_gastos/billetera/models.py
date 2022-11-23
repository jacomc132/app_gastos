from django.db import models


class Billetera(models.Model):
    nombre_billetera = models.CharField(max_length = 40)
    fecha_creacion = models.DateTimeField("date published")
    total_dinero = models.FloatField(default = 0)

    def __str__(self):
        return self.nombre_billetera




class Categoria(models.Model):
    billetera_id = models.ForeignKey(Billetera, on_delete = models.CASCADE)
    nombre_categoria = models.CharField(max_length=40)


    def __str__(self):
        return self.nombre_categoria



class Ingreso(models.Model):
    billetera_id = models.ForeignKey(Billetera, on_delete = models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion_ingreso = models.CharField(max_length = 100)
    valor = models.FloatField(default = 0)
    

    def __str__(self):
        return self.descripcion_ingreso




class Gasto(models.Model):
    billetera_id = models.ForeignKey(Billetera, on_delete = models.CASCADE)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion_gasto = models.CharField(max_length = 100)
    valor = models.FloatField(default = 0)


    def __str__(self):
        return self.descripcion_gasto




