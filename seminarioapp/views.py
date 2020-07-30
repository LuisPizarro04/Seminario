from django.shortcuts import render
from registropaciente.models import paciente
from especialidades.models import Especilidade
from fechas.models import fecha
from seminarioapp.forms import FormReg
from django.http import HttpResponse
from reservar.models import Reserva


# Create your views here.

def home(request):
    return render(request, "home.html")


def registro(request):
    if request.method == "POST":
        form = FormReg(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "gracias.html")
    else:

        form = FormReg()

    return render(request, "registro.html", {'form': form})


def ingreso(request):
    if request.GET["rut"]:
        dato = request.GET["rut"]
        long = len(dato)
        if long != 10:
            return render(request, "ingreso_paciente.html")
        else:
            art = paciente.objects.filter(rut_paciente__contains=dato)
            d1 = Reserva(rut_paciente=dato)
            d1.save()
            return render(request, "datos_paciente.html", {"datos": art, "query": dato})
    else:
        mensaje = "No se ha ingresado ningún rut"

    return HttpResponse(mensaje)


def ingreso_pac(request):
    return render(request, "ingreso_paciente.html")


def esp(request):
    if request.GET["op"]:
        dato = request.GET["op"]
        art = fecha.objects.filter(especialidad__titulo__contains=dato)
        lis = Reserva.objects.all()
        casa = len(lis)
        lis2 = Reserva.objects.values_list('rut_paciente').filter(id_reserva=casa)
        d2 = Reserva(id_reserva=casa, rut_paciente=lis2, especialidad=dato)
        d2.save()
        return render(request, "reservar.html", {"datos": art, "query": dato})
    else:
        mensaje = "No se ha seleccionado ninguna especialidad"
    return HttpResponse(mensaje)


def selesp(request):
    lista = Especilidade.objects.all()
    return render(request, "selec_esp.html", {"lista": lista})


def savedate(request):
    if request.GET["date"]:
        dato = request.GET["date"]
        lis = Reserva.objects.all()
        casa = len(lis)
        lis2 = Reserva.objects.values_list('rut_paciente').filter(id_reserva=casa)
        lis3 = Reserva.objects.values_list('especialidad').filter(id_reserva=casa)
        d3 = Reserva(id_reserva=casa, rut_paciente=lis2, especialidad=lis3, fecha_cita=dato, estado=0)
        d3.save()
        return render(request, "gracR.html")
    else:
        mensaje = "No se ha seleccionado ninguna especialidad"
    return HttpResponse(mensaje)


def reserva(request):
    return render(request, "reservar.html")


def anular(request):
    return render(request, "anular.html")


def cancel(request):
    if request.GET["rut-p"]:
        dato3 = request.GET["rut-p"]
        long = len(dato3)
        if long != 10:
            return render(request, "anular.html")
        else:
            art = Reserva.objects.filter(rut_paciente__contains=dato3, estado=0)
            return render(request, "anulacion.html", {"datos": art, "query": dato3})
    else:
        mensaje = "No se ha ingresado ningún rut"
    return HttpResponse(mensaje)


def savecancel(request):
    if request.GET["patient"]:
        dato4 = request.GET["patient"]
        lis4 = Reserva.objects.filter(rut_paciente=dato4, estado=0).values('id_reserva')
        a = lis4[0]
        b = a['id_reserva']
        lis5 = Reserva.objects.values_list('fecha_cita').filter(id_reserva=b)
        lis6 = Reserva.objects.values_list('especialidad').filter(id_reserva=b)
        sc = Reserva(id_reserva=b, rut_paciente=dato4, especialidad=lis6, fecha_cita=lis5, estado=1)
        sc.save()
        return render(request, "gracN.html")
    else:
        mensaje = "No se ha seleccionado su rut"
    return HttpResponse(mensaje)


def consultar(request):
    return render(request, "consultar.html")


def base(request):
    return render(request, "base.html")


def gracias(request):
    return render(request, "gracias.html")


def prueba(request):
    lista = Especilidade.objects.all()
    return render(request, "pruebea.html", {"lista": lista})
