from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.
def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})

def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    return render (request, 'tareas/detalle.html', {'tarea': tarea})

def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
        return render(request, 'tareas/crear.html', {'form': form})