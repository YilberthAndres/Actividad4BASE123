from django.db import models

from apps.clientes.models import Cliente
from apps.productos.models import Producto
# Create your models here.



class Compra(models.Model):
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.producto