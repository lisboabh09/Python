from django.contrib import admin
from diligencias.models import Diligencia

class DiligenciasAdmin (admin.ModelAdmin):
    list_display = ['nome', 'data_realizacao', 'dinheiro_apreendido']
    search_fields = ['nome']
# Register your models here.
admin.site.register (Diligencia, DiligenciasAdmin)