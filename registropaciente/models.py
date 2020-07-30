from django.db import models


# Create your models here.

class paciente(models.Model):
    FONASA = '01'
    PRAIS = '02'
    CONSALUD = '03'
    CRUZBLANCA = '04'
    COLMENA = '05'
    MASVIDA = '06'
    BANMEDICA = '07'

    PREV_CHOICES = [
        (FONASA, 'Fonasa'),
        (PRAIS, 'Prais'),
        (CONSALUD, 'Consalud'),
        (CRUZBLANCA, 'Cruz blanca'),
        (COLMENA, 'Colmena'),
        (MASVIDA, 'Mas vida'),
        (BANMEDICA, 'Ban Medica'),
    ]

    NINGUNA = '00'
    ALZHEIMER = '01'
    ARTRITIS = '02'
    CANCER = '03'
    DEPRESION = '04'
    DIABETES = '05'
    EPILEPSIA = '06'
    ESCLEROSISM = '07'
    HIPERTENSION = '08'
    PARKINSON = '09'
    TIROIDES = '10'
    ENFER_CHOISES = [(NINGUNA, 'Ninguna'),
                     (ALZHEIMER, 'Alzheimer'),
                     (ARTRITIS, 'Artrítis'),
                     (CANCER, 'Cáncer'),
                     (DEPRESION, 'Depresión'),
                     (DIABETES, 'Diabetes'),
                     (EPILEPSIA, 'Epilepsia'),
                     (ESCLEROSISM, 'Esclerosis múltiple'),
                     (HIPERTENSION, 'Hipertensión'),
                     (PARKINSON, 'Parkinson'),
                     (TIROIDES, 'Tiroides'),
                     ]

    id_registro = models.AutoField(primary_key=True)
    rut_paciente = models.CharField(max_length=10)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    fecha_nac = models.DateField(verbose_name="Fecha de nacimiento: Ejemplo 04/03/1996")
    direccion = models.CharField(max_length=30, verbose_name="Dirección")
    num_casa = models.CharField(max_length=6, verbose_name="Número de casa")
    telefono = models.CharField(max_length=9, verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Correo Electrónico")
    prevision = models.CharField(max_length=20, choices=PREV_CHOICES, default=FONASA, verbose_name="Previsión")
    enf_cro1 = models.CharField(max_length=30, choices=ENFER_CHOISES, default=NINGUNA,
                                verbose_name="Enfermedad crónica 1")
    enf_cro2 = models.CharField(max_length=30, choices=ENFER_CHOISES, default=NINGUNA,
                                verbose_name="Enfermedad crónica 2")
    enf_cro3 = models.CharField(max_length=30, choices=ENFER_CHOISES, default=NINGUNA,
                                verbose_name="Enfermedad crónica 3")
