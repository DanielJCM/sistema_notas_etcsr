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

    nombre_alumno11= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno11= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno11= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno12= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno12= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno12= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno13= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno13= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno13= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno14= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno14= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno14= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno15= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno15= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno15= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno16= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno16= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno16= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno17= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno17= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno17= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno18= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno18= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno18= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno19= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno19= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno19= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno20= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno20= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno20= models.CharField(max_length=2, blank=True,null=True)
    
    nombre_alumno21= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno21= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno21= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno22= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno22= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno22= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno23= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno23= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno23= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno24= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno24= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno24= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno25= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno25= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno25= models.CharField(max_length=2, blank=True,null=True)
    
    nombre_alumno26= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno26= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno26= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno27= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno27= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno27= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno28= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno28= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno28= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno29= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno29= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno29= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno30= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno30= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno30= models.CharField(max_length=2, blank=True,null=True)
    
    nombre_alumno31= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno31= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno31= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno32= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno32= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno32= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno33= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno33= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno33= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno34= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno34= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno34= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno35= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno35= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno35= models.CharField(max_length=2, blank=True,null=True)
    
    nombre_alumno36= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno36= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno36= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno37= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno37= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno37= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno38= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno38= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno38= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno39= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno39= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno39= models.CharField(max_length=2, blank=True,null=True)

    nombre_alumno40= models.CharField(max_length=100, blank=True,null=True)
    cedula_alumno40= models.CharField(max_length=8, blank=True,null=True)
    nota_alumno40= models.CharField(max_length=2, blank=True,null=True)
    def __unicode__(self):
        return self.campo0

    def get_absolute_url(self):
        return reverse('registro:editar_planilla', kwargs={'pk': self.pk})

class Bitacora(models.Model):
    accion = models.CharField(max_length=200, blank=True,null=True)
    fecha = models.CharField(max_length=200, blank=True,null=True)
    
    def __unicode__(self):
        return self.accion