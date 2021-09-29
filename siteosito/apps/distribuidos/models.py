from django.db import models
from apps.productos.models import Producto
from apps.proveedores.models import Proveedore

# Create your models here.

class Distribuido(models.Model):
    productos =  models.ForeignKey(Producto, on_delete=models.CASCADE)
    proveedores =  models.ForeignKey(Proveedore, on_delete=models.CASCADE)