from django import forms
from .models import Carnet_Paciente, Doctor, Farmaceuta, Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        
class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class FarmaceutaForm(forms.ModelForm):
    class Meta:
        model = Farmaceuta
        fields = '__all__'
        
class CarnetForm(forms.ModelForm):
    class Meta:
        model = Carnet_Paciente
        fields = '__all__'