from django.contrib import admin
from especialidades.models import Especilidade

# Register your models here.

class EspecilidadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "cantidad_profesionales", "cantidad_citas")


admin.site.register(Especilidade, EspecilidadAdmin)
