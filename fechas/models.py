from django.db import models
from especialidades.models import Especilidade


# Create your models here.

class fecha(models.Model):
    LIBRE = '0'
    OCUPADA = '1'

    ESTADO_CHOICES = [(LIBRE, 'Libre'), (OCUPADA, 'Ocupada'), ]

    id_cita = models.AutoField(primary_key=True)
    fecha_cita = models.DateTimeField()
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default=LIBRE)
    profesional = models.CharField(max_length=20)
    especialidad = models.ForeignKey('especialidades.Especilidade', on_delete=models.CASCADE)
