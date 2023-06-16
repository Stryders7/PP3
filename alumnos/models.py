from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from typing import Any,Dict, Tuple

# Create your models here.

class Artistas (models.Model):
    nombre_artista   =  models.CharField(max_length=30, blank=False, null=False)
    descripcion      =  models.CharField(max_length=50, blank=False, null=False)
    img              =  models.ImageField(upload_to='img/', null=True, blank=True, verbose_name='img')

def __str__(self):
    return str(self.descripcion)

class Obras (models.Model):
    historia         = models.CharField(max_length=100, blank=False, null=False)
    descripcion      = models.CharField(max_length=50, blank=False, null=False)
    nombre           = models.CharField(max_length=20, blank=False, null=False)
    precio           = models.IntegerField(verbose_name='precio')
    tecnica          = models.CharField(max_length=100, blank=False, null=False)
