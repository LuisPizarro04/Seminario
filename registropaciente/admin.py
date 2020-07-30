from django.contrib import admin
from registropaciente.models import paciente


# Register your models here.

class PacientesAdmin(admin.ModelAdmin):
    list_display = ("rut_paciente", "nombres", "apellidos", "telefono", "prevision", "enf_cro1", "enf_cro2", "enf_cro3")
    search_fields = ("rut_paciente", "prevision")
    list_filter = ("prevision", "fecha_nac")


admin.site.register(paciente, PacientesAdmin)
