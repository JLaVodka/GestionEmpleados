from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_docentes, name='lista_docentes'),
]