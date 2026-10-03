from django.shortcuts import render

from .models import Docente


def lista_docentes(request):
    docentes = Docente.objects.all()

    return render(request, 'docentes/lista.html', {
        'docentes': docentes
    })