from pyexpat import model
from django.db import models
from modulo.medicamento.models import Medicamento
from modulo.usuario.models import Farmaceuta, Carnet_Paciente, Doctor, Paciente


class Prescripcion(models.Model):
    motivo_consulta = models.CharField(max_length=300)
    observacion = models.CharField(max_length=300, blank=True)
    tiempo_uso = models.CharField(max_length=10, blank=True)
    fecha = models.DateField(auto_now=True)
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.DO_NOTHING, verbose_name='Carnet Paciente ')
    idDoctor = models.ForeignKey(Doctor, models.DO_NOTHING)
    
    def __str__(self):
        return str(self.idCarnet_Paciente)
    
class Reg_Entregas(models.Model):
    fecha = models.DateField(auto_now=True)
    idFarmaceuta = models.ForeignKey(Farmaceuta, models.DO_NOTHING)
    idMedicamento = models.ForeignKey(Medicamento, models.DO_NOTHING)
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.CASCADE)
    
    def __str__(self):
        return str(self.idFarmaceuta)
    
class Cita_Medica(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    idPaciente = models.ForeignKey(Paciente, models.CASCADE)
    idDoctor = models.ForeignKey(Doctor, models.CASCADE)
    idPrescripcion =models.ForeignKey(Prescripcion, models.DO_NOTHING)
    
    def __str__(self):
        return str(self.idDoctor)
    

class Reserva(models.Model):
    idCarnet_Paciente = models.ForeignKey(Carnet_Paciente, models.DO_NOTHING)
    idPrescripcion = models.ForeignKey(Prescripcion, models.CASCADE)
    idMedicamento = models.ForeignKey(Medicamento, models.CASCADE)
    cantidad = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return str(self.idCarnet_Paciente)