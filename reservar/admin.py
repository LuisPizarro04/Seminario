from django.contrib import admin
from reservar.models import Reserva


# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display = ("id_reserva", "rut_paciente", "especialidad", "fecha_cita", "estado")


admin.site.register(Reserva, ReservaAdmin)