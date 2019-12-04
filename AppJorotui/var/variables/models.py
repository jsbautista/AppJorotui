from django.db import models


class Variable(models.Model):

    name = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50 )
    imagen = models.CharField(max_length=50 )
    cantidad = models.IntegerField()
    talla = models.CharField(max_length=50)
    costo =  models.CharField(max_length=50)
    estadoInventario = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)
