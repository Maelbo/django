
# Create your views here.
from django.shortcuts import get_object_or_404, render
from computerApp.models import Machine, Personnel

def index(request) :
    machines = Machine.objects.all()
    context = {}
    return render(request, 'index.html', context)

def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request,
     'computerapp/machine_list.html',
     context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine': machine}
    return render(request,
    'computerapp/machine_detail.html',
    context)

def personnel_list_view(request) :
    personnels = Personnel.objects.all()
    context={'personnels': personnels}
    return render(request,
    'computerapp/personnel_list.html',
    context)

def personnel_detail_view(request, pk):
    personnel = get_object_or_404(Personnel, id=pk)
    context={'personnel': personnel}
    return render(request, 'computerapp/personnel_detail.html', context)

