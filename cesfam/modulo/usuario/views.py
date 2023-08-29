from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.

def listar_usuario(request):
    personas = Paciente.objects.all()
    contexto = {
        'form' : personas
    }
    return render(request, 'medico/prueba.html', contexto)
 
def buscar_rut(request):
    
    if request.method == 'GET':
        
        busqueda = request.GET.get("buscar")
        consulta = Paciente.objects.all()
        print(busqueda)
        if busqueda:
            pk = busqueda
            consulta = Paciente.objects.filter(Run = pk)
            print(consulta)
    
    return render(request, 'medico/gg.html', {'persona': consulta})


def enviar_correo(request, pk):
    
    if request.method == 'POST':
        
        asunto = "Medicamentos Disponibles"
        mensaje = "Sus medicamentos recetados por su doctor ya se encuentran disponibles" 
        email_desde =  settings.EMAIL_HOST_USER
        query = Paciente.objects.get(Run = pk)
        print(query)
        email = query.correo
        print(email)
        email_para = [email]
        print()
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently = False)
        return HttpResponse("Correo enviado")
    return render(request, 'medico/gg.html')

    
def crear_paciente(request):
    
    if request.method == 'GET':
        
        paciente = PacienteForm()
        contexto = {
            'form' : paciente
        }

    else:
        paciente = PacienteForm(request.POST)
                
        contexto = {
            'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
            
    return render(request, 'medico/crearpaciente.html', contexto)



def editar_paciente(request, pk):
    persona = Paciente.objects.get(Run = pk)
    
    if request.method == 'GET':
        
        paciente = PacienteForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = PacienteForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, 'medico/prueba.html', contexto)


def eliminar_paciente(request, pk):
    
    persona = Paciente.objects.get(Run = pk)
    persona.delete()
        
    return redirect('buscarrut')



def crear_doctor(request):
    
    if request.method == 'GET':
        
        paciente = DoctorForm()
        contexto = {
            'form' : paciente
        }

    else:
        paciente = DoctorForm(request.POST)
                
        contexto = {
            'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
            
    return render(request, 'medico/crearpaciente.html', contexto)


def editar_doctor(request, pk):
    persona = Doctor.objects.get(Run = pk)
    
    if request.method == 'GET':
        
        paciente = DoctorForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = DoctorForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, 'medico/prueba.html', contexto)


def eliminar_doctor(request, pk):
    
    persona = Doctor.objects.get(Run = pk)
    persona.delete()
        
    return redirect('buscarrut')

def crear_farmaceuta(request):
    
    if request.method == 'GET':
        
        paciente = FarmaceutaForm()
        contexto = {
            'form' : paciente
        }

    else:
        paciente = FarmaceutaForm(request.POST)
                
        contexto = {
            'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
            
    return render(request, 'medico/crearpaciente.html', contexto)


def editar_farmaceuta(request, pk):
    persona = Farmaceuta.objects.get(Run = pk)
    
    if request.method == 'GET':
        
        paciente = FarmaceutaForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = FarmaceutaForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, 'medico/prueba.html', contexto)

def eliminar_farmaceuta(request, pk):
    
    persona = Farmaceuta.objects.get(Run = pk)
    persona.delete()
        
    return redirect('buscarrut')


def crear_carnet(request):
    
    if request.method == 'GET':
        
        paciente = CarnetForm()
        contexto = {
            'form' : paciente
        }

    else:
        paciente = CarnetForm(request.POST)
                
        contexto = {
            'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
            
    return render(request, 'medico/crearpaciente.html', contexto)

def editar_carnet(request, pk):
    persona = Carnet_Paciente.objects.get(id = pk)
    
    if request.method == 'GET':
        
        paciente = CarnetForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = CarnetForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, 'medico/prueba.html', contexto)

def eliminar_carnet(request, pk):
    
    persona = Carnet_Paciente.objects.get(id = pk)
    persona.delete()
        
    return redirect('buscarrut')
