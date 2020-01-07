from django.shortcuts import render
from projectApp.models import Maquina, Status
from django.http import JsonResponse

def status(request):
    context = {}
    return render(request,'status.html', context)

def renderCreateModal(request):
    context = {}
    return render(request,'createStatus.html', context)

def createStatus(request):
    
    nome = ''

    status = Status.get(nome=nome)
    success = False

    if status is not None:
        status.save()
        success = True
    
    return JsonResponse(success, safe=False)

def deleteStatus(request):
    pass

def updateStatus(request):
    pass