from django.contrib import admin
from .models import *

admin.site.register(Proovedor)
admin.site.register(Medicamento)
admin.site.register(Estado_Medicamento)
admin.site.register(Lote)
admin.site.register(Estado_Stock)
admin.site.register(Solicitud_Medicamento)

