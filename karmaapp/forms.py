from django import forms
from .models import *

class CilindroForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['tipo_espuma','num_block','tipo_unidad','no_lote','tipo_ajuste','tipo_defecto','ok_ng','largo','ancho','alto','flujo_de_aire','peso','volumen','densidad']



class FormTest(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['tipo_espuma','num_block','tipo_unidad','no_lote','tipo_ajuste','tipo_defecto','ok_ng','largo','ancho','alto','flujo_de_aire','peso','volumen','densidad']
