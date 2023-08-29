from rest_framework.response import Response
from rest_framework.decorators import api_view
from modulo.medicamento.serializers import *
from modulo.medicamento.models import *


@api_view(['GET','POST'])
def medicamento_api_view(request):
    
    if request.method == 'GET':
        usuarios = Medicamento.objects.all()
        usuarios_serializador = MedicamentoSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = MedicamentoSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def medicamento_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = MedicamentoSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = MedicamentoSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Medicamento.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 
        
        
    
@api_view(['GET','POST'])
def proovedor_api_view(request):
    
    if request.method == 'GET':
        usuarios = Proovedor.objects.all()
        usuarios_serializador = ProovedorSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = ProovedorSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def proovedor_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Proovedor.objects.filter(id = pk).first()
        usuarios_serializador = ProovedorSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Proovedor.objects.filter(id = pk).first()
        usuarios_serializador = ProovedorSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Proovedor.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 



        
@api_view(['GET','POST'])
def estadoStock_api_view(request):
    
    if request.method == 'GET':
        usuarios = Estado_Stock.objects.all()
        usuarios_serializador = EstadoStockSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = EstadoStockSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def estadoStock_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Estado_Stock.objects.filter(id = pk).first()
        usuarios_serializador = EstadoStockSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Estado_Stock.objects.filter(id = pk).first()
        usuarios_serializador = EstadoStockSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Estado_Stock.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error') 
        

@api_view(['GET','POST'])
def estadomedicamento_api_view(request):
    
    if request.method == 'GET':
        usuarios = Estado_Medicamento.objects.all()
        usuarios_serializador = Estado_MedicamentoSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = Estado_MedicamentoSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def estadomedicamento_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Estado_Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = Estado_MedicamentoSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Estado_Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = Estado_MedicamentoSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Estado_Medicamento.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error')
        




@api_view(['GET','POST'])
def solicitudmedi_api_view(request):
    
    if request.method == 'GET':
        usuarios = Solicitud_Medicamento.objects.all()
        usuarios_serializador = SolicitudMediSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = SolicitudMediSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def solicitudmedi_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Solicitud_Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = SolicitudMediSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Solicitud_Medicamento.objects.filter(id = pk).first()
        usuarios_serializador = SolicitudMediSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Solicitud_Medicamento.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error')
        
        



@api_view(['GET','POST'])
def lote_api_view(request):
    
    if request.method == 'GET':
        usuarios = Lote.objects.all()
        usuarios_serializador = LoteSerializer(usuarios, many=True)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'POST':
        usuarios_serializador = LoteSerializer(data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
@api_view(['GET','PUT','DELETE'])
def lote_detail_view(request, pk = None):
    
    if request.method == 'GET':
        usuarios = Lote.objects.filter(id = pk).first()
        usuarios_serializador = LoteSerializer(usuarios)
        return Response(usuarios_serializador.data)
    
    elif request.method == 'PUT':
        usuarios = Lote.objects.filter(id = pk).first()
        usuarios_serializador = LoteSerializer(usuarios, data = request.data)
        if usuarios_serializador.is_valid():
            usuarios_serializador.save()
            return Response(usuarios_serializador.data)
        return Response(usuarios_serializador.errors)
    
    elif request.method == 'DELETE':
        
        if request.method == 'DELETE':
            usuarios = Lote.objects.filter(id = pk).first().delete()
            return Response('Eliminado')
        else:
            return Response('Error')