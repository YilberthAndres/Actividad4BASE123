from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=40)
    precio = models.IntegerField()
    numero_exit = models.IntegerField()
    def __str__(self):
        return self.descripcion