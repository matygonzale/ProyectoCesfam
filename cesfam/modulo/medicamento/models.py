from mailbox import NoSuchMailboxError
from statistics import correlation
from django.db import models
from django.forms import CharField



# Create your models here.

class Estado_Medicamento(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion
    
class Estado_Stock(models.Model):
    descripcion = models.CharField(max_length=50)
    
    def __str__(self):
        return self.descripcion

class Proovedor(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=70)
    correo = models.CharField(max_length=70)
    
    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    peso = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    fecha_caducidad = models.DateField()
    marca = models.CharField(max_length=45)
    stock = models.PositiveSmallIntegerField(default=0)
    stock_critico = models.PositiveSmallIntegerField()
    precio = models.PositiveSmallIntegerField()
    idEstado_Medicamento = models.ForeignKey(Estado_Medicamento, models.DO_NOTHING)
    idProovedor = models.ForeignKey(Proovedor, models.DO_NOTHING)
    idEstado_Stock = models.ForeignKey(Estado_Stock, models.DO_NOTHING)
    
    def __str__(self):
        return self.nombre
    
class Solicitud_Medicamento(models.Model):
    fecha = models.DateField(auto_now=True)
    unidad_solicitada = models.PositiveSmallIntegerField()
    idMedicamento = models.ForeignKey(Medicamento, models.DO_NOTHING)
    
    def __str__(self):
        return str(self.idMedicamento)

class Lote(models.Model):
    cant_cajas = models.PositiveSmallIntegerField()
    unidades_cajas =  models.PositiveSmallIntegerField()
    fecha_recibo = models.DateField()
    elaboracion = models.DateField()
    vencimiento = models.DateField()
    idMedicamento = models.ForeignKey(Medicamento, models.CASCADE)
    
    def __str__(self):
        return str(self.id)
    