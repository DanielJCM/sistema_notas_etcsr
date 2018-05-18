# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Planilla(models.Model):
    """
    Modelo de una planilla.
    """
    campo0 = models.CharField(max_length=100, blank=True,null=True)
    campo1 = models.CharField(max_length=100, blank=True,null=True)
    campo2 = models.CharField(max_length=100, blank=True,null=True)
    campo3 = models.CharField(max_length=100, blank=True,null=True)
    fecha = models.DateField(default=datetime.now, help_text='Fecha')

    # Campos de los alumnos
    nombre_alumno1= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno1= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno1= models.CharField(max_length=2, blank=True,null=True)
    
    nombre_alumno2= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno2= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno2= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno3= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno3= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno3= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno4= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno4= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno4= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno5= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno5= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno5= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno6= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno6= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno6= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno7= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno7= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno7= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno8= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno8= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno8= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno9= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno9= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno9= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno10= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno10= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno10= models.CharField(max_length=2, blank=True,null=True)

    def __unicode__(self):
        return self.entrada    
    def __unicode__(self):
        return self.campo1

    def get_absolute_url(self):
        return reverse('registro:editar_planilla', kwargs={'pk': self.pk})

class Bitacora(models.Model):
    entrada = models.CharField(max_length=200)

    def __unicode__(self):
        return self.entrada