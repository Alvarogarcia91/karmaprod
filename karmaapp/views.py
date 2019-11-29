from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    Block_list = Block.objects.all()
    context ={
        'Block_list':Block_list,
    }
    return render(request, 'index.html',context)

#quitar los que no estan ok para poder pasarlos a peeler o corte
def cilindros(request):
    items = Cilindro.objects.all()
    context ={
        'itemsfront': items,
        #'header':'cilindros',
    }
    return render(request, 'display_espuma.html',context)

#quitar los que no estan ok para poder pasarlos a peeler o corte
def blocks(request):
    items = Block.objects.all()
    context ={
        'itemsfront': items,
        #'header':'blocks',
    }
    return render(request, 'display_espuma.html',context)

def tut(request):
    Cilindro_list = Cilindro.objects.all()
    template = loader.get_template('tut.html')
    context ={
        'Cilindro_list':Cilindro_list,
    }
    return render(request, 'tut.html',context)


def detail_Cilindro(request,item_id):
    item = Cilindro.objects.get(pk=item_id)
    context ={
        'itemsfront':item,
    }

    return render(request, 'detail.html',context)

def detail_Block(request,item_id):
    return HttpResponse("este es el id:  %s" %item_id)


#view para la entrada a peeler
def peeler_Cilindro_entrada(request,cilindro_num):

    return HttpResponse("id del cilindro: %s" % cilindro_num)


def sandbox(request,cilindro_id):
    result = Cilindro.objects.get(pk=cilindro_id)
    context ={
        'result':result,
    }
    return HttpResponse(result)




#querys probados

#lista de todos
# def sandbox(request):
    #Block_list = Block.objects.all()
    #return HttpResponse(Block_list)

#--contador de todo block--
# def sandbox(request):
#     result = Block.objects.count()
#     return HttpResponse(result)


# ---contador de tipo de espuma ----
# def sandbox(request):
#     result = Block.objects.filter(tipo_espuma='24-30').count()
#     return HttpResponse(result)

#--enlistador de todos los blocks
# def index(request):
# Block_list = Block.objects.all()
#
# context ={
#     'Block_list':Block_list,
# }
# return render(request, 'index.html',context)
#
