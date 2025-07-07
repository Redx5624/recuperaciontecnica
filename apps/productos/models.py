from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.TextField("Nombre")
    precio = models.IntegerField("Precio")
    