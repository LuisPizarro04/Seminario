from django.contrib import admin
from fechas.models import fecha


# Register your models here.


class FechaAdmin(admin.ModelAdmin):
    list_display = ("id_cita", "fecha_cita", "estado", "profesional", "especialidad")


admin.site.register(fecha, FechaAdmin)
