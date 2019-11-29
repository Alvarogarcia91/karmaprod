from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello world')
    #return render(request,'index.html')
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
