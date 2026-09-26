from django.shortcuts import render, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from tareas.models import Tarea

# Create your views here.
def lista_empleados(request):
    empleados = Empleado.objects.all()
    context = {'empleados': empleados}
    return render(request, 'empleados/lista.html', context)

def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    tareas_asignadas = Tarea.objects.filter(empleado=empleado_id)
    context = {'empleado': empleado, 'tareas': tareas_asignadas}
    return render(request, 'empleados/detalle.html', context)

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/crear.html', {'form': form})


def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('detalle_empleado', empleado_id=empleado.id)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'empleados/editar.html', {'form': form, 'empleado': empleado})


def eliminar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    tareas_asignadas = Tarea.objects.filter(empleado=empleado_id)

    if request.method == 'POST':
        if tareas_asignadas.exists():
            return render(request, 'empleados/eliminar.html', {
                'empleado': empleado,
                'tareas': tareas_asignadas,
                'error': 'No se puede eliminar: tiene tareas asignadas. Reasígnalas o bórralas primero.',
            })
        empleado.delete()
        return redirect('lista_empleados')

    return render(request, 'empleados/eliminar.html', {'empleado': empleado, 'tareas': tareas_asignadas})
