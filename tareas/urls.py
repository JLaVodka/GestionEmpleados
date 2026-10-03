from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    path('nuevo/', views.crear_tarea, name='crear_tarea'),
    path('<int:tarea_id>/', views.detalle_tarea, name='detalle_tarea'),
    path('asignada/', views.tarea_asignada, name='tarea_asignada'),
    path('consultar-ia/', views.consultar_ia, name='consultar_ia'),
    path('<int:tarea_id>/editar/', views.editar_tarea, name='editar_tarea'),
    path('<int:tarea_id>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
    ]
