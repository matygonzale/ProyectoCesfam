from django import forms
from .models import *


class StockForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['stock']
        
class EstadoMediForm(forms.ModelForm):
    class Meta:
        model = Estado_Medicamento
        fields = '__all__'
        
class EstadoStockForm(forms.ModelForm):
    class Meta:
        model = Estado_Stock
        fields = '__all__'
        
class ProovedorForm(forms.ModelForm):
    class Meta:
        model = Proovedor
        fields = '__all__'
        
class MedicamentoForm(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = '__all__'
        
class SolicitudMediForm(forms.ModelForm):
    class Meta:
        model = Solicitud_Medicamento
        fields = '__all__'

class LoteForm(forms.ModelForm):
    class Meta:
        model = Lote
        fields = '__all__'