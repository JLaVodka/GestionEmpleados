from django.shortcuts import render, get_object_or_404
from .models import Empleado
from tareas.models import Tarea
from microservices import solicitar_con_respaldo

# Create your views here.
def lista_empleados(request):
    try:
        respuesta = solicitar_con_respaldo("/empleados")
        empleados = respuesta.json()
    except Exception as error:
        print(f"Error obteniendo empleados: {error}")
        empleados = []

    return render(
        request,
        "empleados/lista.html",
        {"empleados": empleados}
    )

def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    tareas_asignadas = Tarea.objects.filter(empleado=empleado_id)
    context = {'empleado': empleado, 'tareas': tareas_asignadas}
    return render(request, 'empleados/detalle.html', context)
