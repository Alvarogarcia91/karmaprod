from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.template import loader
from django.db.models import *
from django.db.models import Count
# Create your views here.

def index(request):
    Block_list = Block.objects.all()
    context ={
        'itemsfront':Block_list,
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

def detail(request,item_id):
    item = Cilindro.objects.get(pk=item_id)
    context = {
        'itemsfront':item,
        'header':'cilindros'
    }

    return render(request,'detail.html',context)

def detail_cilindro(request,item_id):
    item = Cilindro.objects.get(pk=item_id)
    context = {
        'itemsfront':item,
        'header':'cilindros'
    }
    return render(request,'detail.html',context)

def detail_block(request,item_id):
    item = Block.objects.get(pk=item_id)
    context = {
        'itemsfront':item,
        'header':'blocks'
    }

    return render(request,'detail.html',context)



def prueba(request):
    Block_list = Block.objects.all()
    context ={
        'itemsfront':Block_list,
    }
    return render(request, 'prueba.html',context)




#view para la entrada a peeler
def peeler_Cilindro_entrada(request,cilindro_num):

    return HttpResponse("id del cilindro: %s" % cilindro_num)


def sandbox(request):
    q1 = Block.objects.all()
    q2 = Cilindro.objects.all()
    q1 = q1.union(q2)
    # context ={
    #     'result':q1,
    # }
    return HttpResponse(q1)

def datatable(request):
    q1 = Block.objects.all()
    q2 = Cilindro.objects.all()
    items = q1.union(q2)
    context ={
        'itemsfront': items,
        #'header':'cilindros',
    }
    return render(request, 'datatable.html',context)


def prueba2(request):
    q1 = Block.objects.all()
    q2 = Cilindro.objects.all()
    items = q1.union(q2)
    context ={
        'itemsfront': items,
        #'header':'cilindros',
    }
    return render(request, 'datatable2.html',context)




def invsum(request):
    conteo = Block.objects.filter(tipo_espuma='15-30').count()
    context ={
        'itemsfront': conteo,
        #'countfront': count,
    }
    #return HttpResponse(result)
    return render(request, 'invsum.html',context)




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
#union de blok y espuma
# def datatable(request):
#     q1 = Block.objects.all()
#     q2 = Cilindro.objects.all()
#     items = q1.union(q2)
#     context ={
#         'itemsfront': items,
#         #'header':'cilindros',
#     }
#     return render(request, 'datatable.html',context)
