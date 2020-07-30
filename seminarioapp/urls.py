from django.urls import path
from seminarioapp import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('reservar', views.reserva, name="Reserva"),
    path('ingreso_paciente', views.ingreso_pac, name="IngresoPac"),
    path('selesp', views.selesp, name="Seleccionar"),
    path('esp/', views.esp, name="Esp"),
    path('savedate/', views.savedate, name="SD"),
    path('ingreso/', views.ingreso, name="Ingreso"),
    path('anular', views.anular, name="Anular"),
    path('cancel/', views.cancel, name="Anulacion"),
    path('savecancel/', views.savecancel, name="SaveCancel"),
    path('registro', views.registro, name="Registro"),
    path('consultar', views.consultar, name="Consultar"),
    path('base', views.consultar, name="Base"),
    path('gracias', views.gracias, name="Gracias"),
    path('pruebea', views.prueba, name="Prueba")
]
