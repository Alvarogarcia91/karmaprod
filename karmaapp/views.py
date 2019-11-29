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
    return HttpResponse(template.render(context,request))



def tut(request):
    Block_list = Block.objects.all()
    template = loader.get_template('tut.html')
    context ={
        'Block_list':Block_list,

    }
    return render(request, 'tut.html',context)


def datatables(request):
    Block_list = Block.objects.all()
    template = loader.get_template('datatables.html')
    context ={
        'Block_list':Block_list,

    }
    return render(request, 'tut.html',context)



def sandbox(request):
    result = Block.objects.filter(tipo_espuma='24-30').count()
    return HttpResponse(result)




#querys probados

#lista de todos
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
