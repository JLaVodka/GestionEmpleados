from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarea
from .forms import TareaForm
import requests


def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas/lista.html', {'tareas': tareas})


def detalle_tarea(request, tarea_id):
    tarea = get_object_or_404(Tarea, id=tarea_id)
    context = {'tarea': tarea}
    return render(request, 'tareas/detalle.html', context)


def crear_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    return render(request, 'tareas/crear.html', {'form': form})


def tarea_asignada(request):
    try:
        respuesta = requests.get(
            'https://backend-empleados-9oud.onrender.com/empleados',
            timeout=30)
        respuesta.raise_for_status()
        datos = respuesta.json()
    except requests.RequestException:
        datos = None

    context = {'datos': datos}
    return render(request, 'tareas/asignada.html', context)
