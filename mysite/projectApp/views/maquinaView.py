from django.shortcuts import render
from projectApp.models import Maquina, Status

def maquinas(request):
    context = {}
    return render(request,'maquinas.html', context)

def createMaquina(request):
    
    nome = request.POST.get('nome')
    statusName = request.POST.get('status')

    status = Status.get(nome=statusName)
    if nome:
        status = Status.get(nome=statusName)
        statusId = status.id
        maquina.save()

def deleteMaquina(request):
    pass

def updateMaquina(request):
    pass