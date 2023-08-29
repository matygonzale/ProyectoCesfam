from django.db import models
from django.contrib.auth.models import User

class Carnet_Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    consultorio = models.CharField(max_length=30)
    color = models.CharField(max_length=30, verbose_name='Rojo/Amarillo/Verde')
    
    def __str__(self):
        return self.nombre
    
class Paciente(models.Model):
    Run = models.PositiveBigIntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=13)
    cronico = models.CharField(max_length=2)
    tutor = models.CharField(max_length=60, blank=True)
    telefono_tutor = models.CharField(max_length=13, blank=True)
    nacimiento = models.DateField()
    direccion = models.CharField(max_length=70)
    genero = models.CharField(max_length=9, verbose_name='Genero:(M / F)')
    correo = models.EmailField(max_length=150, unique=True)
    idCarnet_Paciente = models.OneToOneField(Carnet_Paciente, models.CASCADE)
    
    def __str__(self):
        return self.nombre
    
class Doctor(models.Model):
    Run = models.PositiveBigIntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, verbose_name='Genero:(M / F)')
    nacimiento = models.DateField()
    especialidad = models.CharField(max_length=50)
    correo = models.EmailField(max_length=150, unique=True)
    telefono = models.CharField(max_length=13)
    direccion = models.CharField(max_length=70)
    idUser = models.OneToOneField(User, models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nombre
    
class Farmaceuta(models.Model):
    Run = models.PositiveBigIntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField()
    telefono = models.CharField(max_length=13)
    genero = models.CharField(max_length=1, verbose_name='Genero:(M / F)')
    puesto = models.CharField(max_length=50)
    idUser = models.OneToOneField(User, models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.nombre