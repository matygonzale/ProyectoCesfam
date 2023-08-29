from django.shortcuts import redirect, render
from django.template import ContextPopException
from modulo.medicamento.models import *
from modulo.medicamento.forms import *


# Create your views here.

def listar_medicamento(request):
    medi = Medicamento.objects.all()
    contexto = {
        'form' : medi
    }
    return render(request, 'medico/prueba.html', contexto)


def buscar_medicamento(request):
    
    if request.method == 'GET':
        
        busqueda = request.GET.get("buscar")
        consulta = Medicamento.objects.all()
        
        if busqueda:
            pk = busqueda
            consulta = Medicamento.objects.filter(id = pk)
            
            
    return render(request, 'medico/gg.html', {'medicamento': consulta})


def crear_estadomedicamento(request):
    
    if request.method == 'GET':
        
        estado = EstadoMediForm()
        contexto = {
            'form' : estado
        }

    else:
        estado= EstadoMediForm(request.POST)
                
        contexto = {
            'form' : estado
        }
        if estado.is_valid():
            estado.save()
            
    return render(request, '', contexto)


def editar_estadomedicamento(request, pk):
    medi = Estado_Medicamento.objects.get(id = pk)
    
    if request.method == 'GET':
        
        estado = EstadoMediForm(instance = medi)
        contexto = {
            'form' : estado
        }
    elif request.method == 'POST':
        
        estado = EstadoMediForm(request.POST, instance = medi)
        
        contexto = {
        'form' : estado
        }
        if estado.is_valid():
            estado.save()
    return render(request, '', contexto)

def eliminar_estadomedicamento(request, pk):
    
    estado = Estado_Medicamento.objects.get(id = pk)
    estado.delete()
        
    return redirect('')



def crear_estadostock(request):
    
    if request.method == 'GET':
        
        estado = EstadoStockForm()
        contexto = {
            'form' : estado
        }

    else:
        estado= EstadoStockForm(request.POST)
                
        contexto = {
            'form' : estado
        }
        if estado.is_valid():
            estado.save()
            
    return render(request, '', contexto)

def editar_estadostock(request, pk):
    medi = Estado_Stock.objects.get(id = pk)
    
    if request.method == 'GET':
        
        estado = EstadoStockForm(instance = medi)
        contexto = {
            'form' : estado
        }
    elif request.method == 'POST':
        
        estado = EstadoStockForm(request.POST, instance = medi)
        
        contexto = {
        'form' : estado
        }
        if estado.is_valid():
            estado.save()
    return render(request, '', contexto)

def eliminar_estadostock(request, pk):
    
    estado = Estado_Stock.objects.get(id = pk)
    estado.delete()
        
    return redirect('')



def crear_proovedor(request):
    
    if request.method == 'GET':
        
        proovedor = ProovedorForm()
        contexto = {
            'form' : proovedor
        }

    else:
        proovedor= ProovedorForm(request.POST)
                
        contexto = {
            'form' : proovedor
        }
        if proovedor.is_valid():
            proovedor.save()
            
    return render(request, '', contexto)

def editar_proovedor(request, pk):
    consulta = Proovedor.objects.get(id = pk)
    
    if request.method == 'GET':
        
        proovedor = ProovedorForm(instance = consulta)
        contexto = {
            'form' : proovedor
        }
    elif request.method == 'POST':
        
        proovedor = ProovedorForm(request.POST, instance = consulta)
        
        contexto = {
        'form' : proovedor
        }
        if proovedor.is_valid():
            proovedor.save()
    return render(request, '', contexto)

def eliminar_proovedor(request, pk):
    
    proovedor = Proovedor.objects.get(id = pk)
    proovedor.delete()
        
    return redirect('')




def crear_medicamento(request):
    
    if request.method == 'GET':
        
        medi = MedicamentoForm()
        contexto = {
            'form' : medi
        }

    else:
        medi= MedicamentoForm(request.POST)
                
        contexto = {
            'form' : medi
        }
        if medi.is_valid():
            medi.save()
            
    return render(request, '', contexto)

def editar_medicamento(request, pk):
    consulta = Medicamento.objects.get(id = pk)
    
    if request.method == 'GET':
        
        medi = MedicamentoForm(instance = consulta)
        contexto = {
            'form' : medi
        }
    elif request.method == 'POST':
        
        medi = MedicamentoForm(request.POST, instance = consulta)
        
        contexto = {
        'form' : medi
        }
        if medi.is_valid():
            medi.save()
    return render(request, '', contexto)

def eliminar_medicamento(request, pk):
    
    medi = Medicamento.objects.get(id = pk)
    medi.delete()
        
    return redirect('')




def crear_solicitudmedi(request):
    
    if request.method == 'GET':
        
        medi = SolicitudMediForm()
        contexto = {
            'form' : medi
        }

    else:
        medi= SolicitudMediForm(request.POST)
                
        contexto = {
            'form' : medi
        }
        if medi.is_valid():
            medi.save()
            
    return render(request, '', contexto)

def editar_solicitudmedi(request, pk):
    consulta = Solicitud_Medicamento.objects.get(id = pk)
    
    if request.method == 'GET':
        
        medi = SolicitudMediForm(instance = consulta)
        contexto = {
            'form' : medi
        }
    elif request.method == 'POST':
        
        medi = SolicitudMediForm(request.POST, instance = consulta)
        
        contexto = {
        'form' : medi
        }
        if medi.is_valid():
            medi.save()
    return render(request, '', contexto)

def eliminar_solicitudmedi(request, pk):
    
    medi = Solicitud_Medicamento.objects.get(id = pk)
    medi.delete()
        
    return redirect('')



def crear_lote(request):
    
    if request.method == 'GET':
        
        lote = LoteForm()
        contexto = {
            'form' : lote
        }

    else:
        lote= LoteForm(request.POST)
                
        contexto = {
            'form' : lote
        }
        if lote.is_valid():
            lote.save()
            
    return render(request, '', contexto)

def editar_lote(request, pk):
    consulta = Lote.objects.get(id = pk)
    
    if request.method == 'GET':
        
        lote = LoteForm(instance = consulta)
        contexto = {
            'form' : lote
        }
    elif request.method == 'POST':
        
        lote = LoteForm(request.POST, instance = consulta)
        
        contexto = {
        'form' : lote
        }
        if lote.is_valid():
            lote.save()
    return render(request, '', contexto)

def eliminar_lote(request, pk):
    
    lote = Lote.objects.get(id = pk)
    lote.delete()
        
    return redirect('')