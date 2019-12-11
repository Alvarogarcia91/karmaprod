from django import forms
from .models import *

class CilindroForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['tipo_espuma','num_block','tipo_unidad','no_lote','tipo_ajuste','tipo_defecto','ok_ng','largo','ancho','alto','flujo_de_aire','peso','volumen','densidad','dispobible']


#notaaa para el curado usa el modelform

#prueba del formmodel

class FormTest(forms.ModelForm):
    tipo_espuma = forms.CharField(error_messages={'required': 'Escriba el tipo de espuma'})
    num_block = forms.CharField(error_messages={'required': 'Escriba el Numero de Block si no como identificaremos cual pieza es...)'})
    no_lote = forms.CharField(error_messages={'required': 'Escriba el Numero De Lote (si no como identificaremos cual es el lote de la pieza...)'})
    ok_ng = forms.CharField(error_messages={'required': 'ok? not good? este es el primer filtro de calidad'})
    largo = forms.CharField(error_messages={'required': 'Escriba el largo ,2 decimales max'}) 
    ancho = forms.CharField(error_messages={'required': 'Escriba el ancho,2 decimales max'}) 
    flujo_de_aire = forms.CharField(error_messages={'required': 'Escriba el flujo_de_aire,2 decimales max'}) 
    peso = forms.CharField(error_messages={'required': 'Escriba el peso,2 decimales max'})
    volumen = forms.CharField(error_messages={'required': 'Escriba el volumen,2 decimales max'})
    densidad = forms.CharField(error_messages={'required': 'Escriba la densidad,2 decimales max'})   
    class Meta:
        model = Cilindro
        fields = ['tipo_espuma','num_block','tipo_unidad','no_lote','tipo_ajuste','tipo_defecto','ok_ng','largo','ancho','alto','flujo_de_aire','peso','volumen','densidad']
       


class MedidasCuradasForm(forms.ModelForm):
    class Meta:
        model = Cilindro
        fields = ['largo_curado','ancho_curado','alto_curado','volumen_curado','densidad_curado','auth_corte','dispobible']
       


#version LARGA
# class FormTest(forms.Form):
#     tipo_espuma = forms.CharField(label='Tipo de Espuma', max_length=100,error_messages={'required': 'Please let us know what to call you!'})
#     num_block = forms.IntegerField(label='Numero de Block')
#     tipo_unidad = forms.CharField(label='Tipo de Unidad', max_length=100)
#     no_lote = forms.CharField(label='Numero de Lote', max_length=100)
#     tipo_ajuste = forms.CharField(label='Tipo de Ajuste', max_length=100)
#     tipo_defecto = forms.CharField(label='Tipo de Defecto', max_length=100)
#     ok_ng = forms.CharField(label='ok/ng', max_length=100)
#     largo = forms.DecimalField(label='Largo',max_digits=10, decimal_places=2)
#     ancho = forms.DecimalField(label='Ancho',max_digits=10, decimal_places=2)
#     alto = forms.DecimalField(label='Alto',max_digits=10, decimal_places=2)
#     flujo_de_aire = forms.DecimalField(label='Flujo De Aire',max_digits=10, decimal_places=2)
#     peso = forms.DecimalField(label='Peso',max_digits=10, decimal_places=2)
#     volumen = forms.DecimalField(label='Volumen',max_digits=10, decimal_places=2)
#     densidad = forms.DecimalField(label='Densidad',max_digits=10, decimal_places=2)
#     source = forms.CharField(       # A hidden input for internal use
#         max_length=50,              # tell from which page the user sent the message
#         widget=forms.HiddenInput()
#     )

# def clean(self):
#     cleaned_data = super(FormTest, self).clean()
#     tipo_espuma = cleaned_data.get('tipo_espuma')
#     num_block = cleaned_data.get('num_block')
#     tipo_unidad = cleaned_data.get('tipo_unidad')
#     no_lote = cleaned_data.get('no_lote')
#     tipo_ajuste = cleaned_data.get('tipo_ajuste')
#     tipo_defecto = cleaned_data.get('tipo_defecto')
#     ok_ng = cleaned_data.get('ok_ng')
#     largo = cleaned_data.get('largo')
#     ancho = cleaned_data.get('ancho')
#     alto = cleaned_data.get('alto')
#     flujo_de_aire = cleaned_data.get('flujo_de_aire')
#     peso = cleaned_data.get('peso')
#     volumen = cleaned_data.get('volumen')
#     densidad = cleaned_data.get('densidad')
    

