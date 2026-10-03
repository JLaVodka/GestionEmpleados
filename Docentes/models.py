from django.db import models

# Create your models here.
from django.db import models


class Docente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    imagen = models.CharField(max_length=1500)

    def __str__(self):
        return self.nombre