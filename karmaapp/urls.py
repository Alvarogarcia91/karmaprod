from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('cilindros/',views.cilindros,name='cilindros'),
    path('blocks/',views.blocks,name='blocks'),
    #--la variable item_id es la que va alado del request en la view
    path('cilindros/<int:item_id>/',views.detail_Cilindro,name='detail_Cilindro'),
    path('blocks/<int:item_id>/',views.detail_Block,name='detail_Block'),


    path('peeler_cilindro_entrada/<int:cilindro_num>/',views.peeler_Cilindro_entrada,name='peeler_Cilindro_entrada'),

    path('sandbox/',views.sandbox,name='sandbox'),
    path('tut/',views.tut,name='tut'),

    #
]
