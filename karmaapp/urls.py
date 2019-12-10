from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('cilindros/',views.cilindros,name='cilindros'),
    path('blocks/',views.blocks,name='blocks'),
    #--la variable item_id es la que va alado del request en la view

    #path('cilindros/<int:item_id>/',views.detail,name='detail'),
    path('cilindros/<int:item_id>/',views.detail_cilindro,name='detail_cilindro'),
    path('blocks/<int:item_id>/',views.detail_block,name='detail_block'),


    path('datatable/',views.datatable,name='datatable'),
    #path para Capturar
    #path('capturar_block/',views.alta_blocks,name='alta_blocks'),
    path('capturar_cilindro/',views.alta_cilindro,name='alta_cilindro'),


    path('prueba2/',views.prueba2,name='prueba2'),

    path('invsum/',views.invsum,name='invsum'),


    path('prueba/',views.prueba,name='prueba'),
    path('peeler_cilindro_entrada/<int:cilindro_num>/',views.peeler_Cilindro_entrada,name='peeler_Cilindro_entrada'),

    path('sandbox/',views.sandbox,name='sandbox'),
    path('tut/',views.tut,name='tut'),
    path('sandbox2/',views.sandbox2,name='sandbox2'),
    
    path('formtest/',views.formtest,name='formtest'),
    #
]
