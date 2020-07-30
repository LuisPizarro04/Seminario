from django.db import models


# Create your models here.

class Especilidade(models.Model):
    titulo = models.CharField(primary_key=True, max_length=30, unique=True)
    cantidad_profesionales = models.IntegerField()
    cantidad_citas = models.IntegerField()

   # def __str__(self):
    #    return self.titulo
