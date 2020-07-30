from registropaciente.models import paciente
from reservar.models import Reserva
from django.forms import ModelForm


class FormReg(ModelForm):
    class Meta:
        model = paciente
        fields = ['id_registro', 'rut_paciente', 'nombres', 'apellidos', 'fecha_nac', 'direccion', 'num_casa',
                  'telefono', 'email', 'prevision', 'enf_cro1', 'enf_cro2', 'enf_cro3']


class FormRes(ModelForm):
    class Meta:
        model = Reserva
        fields = ['especialidad']
