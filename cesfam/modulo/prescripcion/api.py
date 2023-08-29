from rest_framework.response import Response
from rest_framework.decorators import api_view
from modulo.prescripcion.serializers import *
from modulo.prescripcion.models import *


@api_view(['GET','POST'])
def prescripcion_api_view(request):
    
    if request.method == 'GET':
        usuarios = Prescripcion.objects.all()
        usuarios_serializador = PrescripcionSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = PrescripcionSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def prescripcion_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Prescripcion.objects.filter(id = pk).first()
        usuarios_serializador = PrescripcionSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Prescripcion.objects.filter(id = pk).first()
        usuarios_serializador = PrescripcionSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Prescripcion.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 
        


@api_view(['GET','POST'])
def entregas_api_view(request):
    
    if request.method == 'GET':
        usuarios = Reg_Entregas.objects.all()
        usuarios_serializador = Reg_EntregasSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = Reg_EntregasSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def entregas_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Reg_Entregas.objects.filter(id = pk).first()
        usuarios_serializador = Reg_EntregasSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Reg_Entregas.objects.filter(id = pk).first()
        usuarios_serializador = Reg_EntregasSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Reg_Entregas.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 
        


@api_view(['GET','POST'])
def cita_api_view(request):
    
    if request.method == 'GET':
        usuarios = Cita_Medica.objects.all()
        usuarios_serializador = Cita_MedicaSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = Cita_MedicaSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)

@api_view(['GET','PUT','DELETE'])
def cita_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Cita_Medica.objects.filter(id = pk).first()
        usuarios_serializador = Cita_MedicaSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Reg_Entregas.objects.filter(id = pk).first()
        usuarios_serializador = Cita_MedicaSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Cita_Medica.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 
        



@api_view(['GET','POST'])
def reserva_api_view(request):
    
    if request.method == 'GET':
        usuarios = Reserva.objects.all()
        usuarios_serializador = ReservaSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = ReservaSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def reserva_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Reserva.objects.filter(id = pk).first()
        usuarios_serializador = ReservaSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Reserva.objects.filter(id = pk).first()
        usuarios_serializador = ReservaSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Reserva.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 