from rest_framework.response import Response
from rest_framework.decorators import api_view
from modulo.usuario.serializers import *
from modulo.usuario.models import *

@api_view(['GET','POST'])
def paciente_api_view(request):
    
    if request.method == 'GET':
        usuarios = Paciente.objects.all()
        usuarios_serializador = PacienteSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = PacienteSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def paciente_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Paciente.objects.filter(Run = pk).first()
        usuarios_serializador = PacienteSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Paciente.objects.filter(Run = pk).first()
        usuarios_serializador = PacienteSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors) 
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Paciente.objects.filter(Run = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error')
        
    
    
@api_view(['GET','POST'])
def doctor_api_view(request):
    
    if request.method == 'GET':
        usuarios = Doctor.objects.all()
        usuarios_serializador = DoctorSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = DoctorSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def doctor_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Doctor.objects.filter(Run = pk).first()
        usuarios_serializador = DoctorSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Doctor.objects.filter(Run = pk).first()
        usuarios_serializador = DoctorSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)

    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Doctor.objects.filter(Run = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Hubo un Error')
        
        

@api_view(['GET','POST'])
def farmaceuta_api_view(request):
    
    if request.method == 'GET':
        usuarios = Farmaceuta.objects.all()
        usuarios_serializador = FarmaceutaSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = FarmaceutaSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def farmaceuta_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Farmaceuta.objects.filter(Run = pk).first()
        usuarios_serializador = FarmaceutaSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Farmaceuta.objects.filter(Run = pk).first()
        usuarios_serializador = FarmaceutaSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Farmaceuta.objects.filter(Run = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Hubo un Error')
        
@api_view(['GET','POST'])
def carnet_api_view(request):
    
    if request.method == 'GET':
        usuarios = Carnet_Paciente.objects.all()
        usuarios_serializador = Carnet_PacienteSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = Carnet_PacienteSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def carnet_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Carnet_Paciente.objects.filter(id = pk).first()
        usuarios_serializador = Carnet_PacienteSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Carnet_Paciente.objects.filter(id = pk).first()
        usuarios_serializador = Carnet_PacienteSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Carnet_Paciente.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Hubo un Error')
        
        

@api_view(['GET','POST'])
def user_api_view(request):
    
    if request.method == 'GET':
        usuarios = User.objects.all()
        usuarios_serializador = UserSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = UserSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = User.objects.filter(username = pk).first()
        usuarios_serializador = UserSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = User.objects.filter(username = pk).first()
        usuarios_serializador = UserSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = User.objects.filter(username = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Hubo un Error')