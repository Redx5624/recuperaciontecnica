from django.db import models

# Create your models here.
class Debito(models.Model):
    acumulado = models.IntegerField("Acumulado")
    valor = models.IntegerField("valor")