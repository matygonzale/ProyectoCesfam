from django import forms
from .models import *

class PrescripcionForm(forms.ModelForm):
    class Meta:
        model = Prescripcion
        fields = '__all__'
        
class EntregasForm(forms.ModelForm):
    class Meta:
        model = Reg_Entregas
        fields = '__all__'
        
class Cita_MedicaForm(forms.ModelForm):
    class Meta:
        model = Cita_Medica
        fields = '__all__'
        
class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'