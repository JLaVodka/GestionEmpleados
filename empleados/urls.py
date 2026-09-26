from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_empleados, name='lista_empleados'),
    path('<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('nuevo/', views.crear_empleado, name='crear_empleado'),
    path('<int:empleado_id>/editar/', views.editar_empleado, name='editar_empleado'),
    path('<int:empleado_id>/eliminar/', views.eliminar_empleado, name='eliminar_empleado'),
    ]
