from django.urls import path
from modulo.prescripcion.api import *
from modulo.prescripcion.views import *


urlpatterns = [
    path('prescripcion/', prescripcion_api_view, name='prescripcion_api'),
    path('prescripcion/<int:pk>/', prescripcion_detail_view, name='prescripcion_detail_api' ),
    path('reg_entregas/', entregas_api_view, name='reg_entrega_api'),
    path('reg_entregas/<int:pk>/', entregas_detail_view, name= 'reg_entrega_detail_api'),
    path('citamedica/', cita_api_view, name='citamedica_api'),
    path('citamedica/<int:pk>/', cita_detail_view, name='citamedica_detail_api'),
    path('reserva/', reserva_api_view, name='reserva_api'),
    path('reserva/<int:pk>/', reserva_detail_view, name='reserva_detail_api'),
    path('listar/', listar_prescripcion, name='listarprescripcion'),
    path('buscarprescripcion/', buscar_prescripcion, name= 'buscarprescripcion'),
    path('crearprescripcion/', crear_prescripcion, name='crearprescripcion'),
    path('editarprescripcion/<int:pk>/', editar_prescripcion, name='editarprescripcion'),
    path('eliminarprescripcion/<int:pk>/', eliminar_prescripcion, name='eliminarprescripcion'),
    path('crearregentrega/', crear_regEntrega, name='crearregentrega'),
    path('editarregentrega/<int:pk>/', editar_regEntrega, name='editarregentrega'),
    path('eliminarregentrega/<int:pk>/', eliminar_regEntrega, name='eliminarregentrega'),
    path('crearcitamedica/', crear_citamedica, name='crearcitamedica'),
    path('editarcitamedica/<int:pk>/', editar_citamedica, name='editarcitamedica'),
    path('eliminarcitamedica/<int:pk>/', eliminar_citamedica, name='eliminarcitamedica'),
    path('crearreserva/', crear_reserva, name='crearreserva'),
    path('eliminarreserva/<int:pk>/', eliminar_reserva, name='eliminarreserva')
]



