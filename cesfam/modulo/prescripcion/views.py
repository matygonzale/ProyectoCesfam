from django.http import HttpResponse
from modulo.prescripcion.forms import *
from django.shortcuts import redirect, render
from .models import *
from modulo.medicamento.models import Medicamento


def listar_prescripcion(request):
    pres = Prescripcion.objects.all()
    contexto = {
        'form' : pres
    }
    return render(request, 'medico/prueba.html', contexto)


def buscar_prescripcion(request):
    busqueda = request.GET.get("buscar")
    consulta = Prescripcion.objects.all()
    
    if busqueda!="":
        pk = busqueda
        consulta = Prescripcion.objects.filter(id = pk)
        
    return render(request, 'medico/gg.html', {'prescripcion': consulta})


def crear_prescripcion(request):
    
    if request.method == 'GET':
        
        prescripcion = PrescripcionForm()
        contexto = {
            'form' : prescripcion
        }

    else:
        paciente = PrescripcionForm(request.POST)
                
        contexto = {
            'form' : prescripcion
        }
        if prescripcion.is_valid():
            prescripcion.save()
            
    return render(request, '', contexto)

def editar_prescripcion(request, pk):
    persona = Prescripcion.objects.get(id = pk)
    
    if request.method == 'GET':
        
        prescripcion = PrescripcionForm(instance = persona)
        contexto = {
            'form' : prescripcion
        }
    elif request.method == 'POST':
        
        prescripcion = PrescripcionForm(request.POST, instance = persona)
        
        contexto = {
        'form' : prescripcion
        }
        if prescripcion.is_valid():
            prescripcion.save()
    return render(request, '', contexto)

def eliminar_prescripcion(request, pk):
    
    persona = Prescripcion.objects.get(id = pk)
    persona.delete()
        
    return redirect()


def crear_regEntrega(request):
    
    if request.method == 'GET':
        
        regentrega = EntregasForm()
        contexto = {
            'form' : regentrega
        }

    else:
        regentrega = EntregasForm(request.POST)
                
        contexto = {
            'form' : regentrega
        }
        if regentrega.is_valid():
            regentrega.save()
            
    return render(request, '', contexto)

def editar_regEntrega(request, pk):
    persona = Reg_Entregas.objects.get(id = pk)
    
    if request.method == 'GET':
        
        paciente = EntregasForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = EntregasForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, '', contexto)

def eliminar_regEntrega(request, pk):
    
    persona = Reg_Entregas.objects.get(id = pk)
    persona.delete()
        
    return redirect('')



def crear_citamedica(request):
    
    if request.method == 'GET':
        
        citamed = Cita_MedicaForm()
        contexto = {
            'form' : citamed
        }

    else:
        citamed= Cita_MedicaForm(request.POST)
                
        contexto = {
            'form' : citamed
        }
        if citamed.is_valid():
            citamed.save()
            
    return render(request, '', contexto)

def editar_citamedica(request, pk):
    persona = Cita_Medica.objects.get(id = pk)
    
    if request.method == 'GET':
        
        paciente = Cita_MedicaForm(instance = persona)
        contexto = {
            'form' : paciente
        }
    elif request.method == 'POST':
        
        paciente = Cita_MedicaForm(request.POST, instance = persona)
        
        contexto = {
        'form' : paciente
        }
        if paciente.is_valid():
            paciente.save()
    return render(request, '', contexto)

def eliminar_citamedica(request, pk):
    
    persona = Cita_Medica.objects.get(id = pk)
    persona.delete()
        
    return redirect('')



def crear_reserva(request):
    
    if request.method == 'GET':
        
        reserva = ReservaForm()
        contexto = {
            'form' : reserva
        }

    if request.method == 'POST':
        
        citamed= ReservaForm(request.POST)
        cantidad = request.POST['cantidad']
        pk = request.POST['idMedicamento']
        consulta = Medicamento.objects.get(id = pk)
        
        z = consulta.id
        a = consulta.nombre
        b = consulta.peso
        c = consulta.tipo
        d = consulta.fecha_caducidad
        e = consulta.marca
        stock = consulta.stock
        f = consulta.stock_critico
        g = consulta.precio
        h = consulta.idEstado_Medicamento
        i = consulta.idProovedor
        j = consulta.idEstado_Stock
        
        reserva = stock - int(cantidad)
        
        contexto = {'form': citamed, 'reserva': reserva}
        
        if reserva >= 0:
            medi = Medicamento()
            medi.id = z
            medi.nombre = a 
            medi.peso = b
            medi.tipo = c
            medi.fecha_caducidad = d
            medi.marca = e
            medi.stock = reserva
            medi.stock_critico = f
            medi.precio = g
            medi.idEstado_Medicamento = h
            medi.idProovedor = i
            medi.idEstado_Stock = j
            medi.save()
            
            if citamed.is_valid():
                citamed.save()
        else:
            return HttpResponse('No se pudo hacer la reserva')
            
    return render(request, 'medico/gg.html', contexto)


def eliminar_reserva(request, pk):
    
    consulta1 = Reserva.objects.get(id = pk)
    cantidad = consulta1.cantidad
    medi = consulta1.idMedicamento_id
    pk2 = int(medi)
    consulta2 = Medicamento.objects.get(id = pk2)
    
    z = consulta2.id
    a = consulta2.nombre
    b = consulta2.peso
    c = consulta2.tipo
    d = consulta2.fecha_caducidad
    e = consulta2.marca
    stock = consulta2.stock
    f = consulta2.stock_critico
    g = consulta2.precio
    h = consulta2.idEstado_Medicamento
    i = consulta2.idProovedor
    j = consulta2.idEstado_Stock
    
    reserva = int(cantidad) + stock 
    
    if reserva >= 0:
        
        medi = Medicamento()
        medi.id = z
        medi.nombre = a 
        medi.peso = b
        medi.tipo = c
        medi.fecha_caducidad = d
        medi.marca = e
        medi.stock = reserva
        medi.stock_critico = f
        medi.precio = g
        medi.idEstado_Medicamento = h
        medi.idProovedor = i
        medi.idEstado_Stock = j
        medi.save()
        consulta1.delete()
        
    return redirect('crearreserva')