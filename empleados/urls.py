from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_empleados, name='lista_empleados'),
    path('<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    ]