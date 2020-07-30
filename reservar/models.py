from django.db import models
from especialidades.models import Especilidade


# Create your models here.

class Reserva(models.Model):
    ACTIVA = '0'
    INACTIVA = '1'

    ESTADO_CHOICES = [(ACTIVA, 'Activa'), (INACTIVA, 'Inactiva'), ]

    id_reserva = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=10)
    especialidad = models.CharField(max_length=40, null=True)
    fecha_cita = models.DateTimeField(blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES, default=None, null=True)


