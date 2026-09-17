from django.shortcuts import render, get_object_or_404
from .models import Empleado
from tareas.models import Tarea

# Create your views here.
def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista.html', {'empleados': empleados})

def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    tareas_asignadas = Tarea.objects.filter(empleado=empleado_id)
    return render(request, 'empleados/detalle.html',{'empleado': empleado, 'tareas':tareas_asignadas})
