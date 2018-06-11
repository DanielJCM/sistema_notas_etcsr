# -*- coding: utf-8 -*-
from django import forms
from registro.models import Planilla
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget

secciones = (
    ('A', 'Sección A'),
    ('B', 'Sección B'),
    ('C', 'Sección C'),
    ('D', 'Sección D'),
    ('E', 'Sección E'),
    ('F', 'Sección F')
)

sit_jur = (
    ('-', '-'),
    ('Propio', 'Propio'),
    ('Comodato', 'Comodato'),
    ('Préstamo', 'Préstamo'),
)
estados = (
    ('-', '-'),
    ('Operativo','Operativo'),
    ('Averiado','Averiado'),
    ('En reparación','En reparación'),
    ('Desuso','Desuso'),
    ('Desincorporado','Desincorporado'),
)

class PlanillaForm(forms.ModelForm):
    """
    Formulario con los campos de una planilla.
    """
    campo0 = forms.CharField(label='Nombre del Profesor', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo1 = forms.CharField(label='Materia', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo2 = forms.CharField(label='Mención', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo3 = forms.ChoiceField(label='Sección', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = secciones)

    fecha = forms.CharField(label='Fecha', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: none;',
        #'placeholder': des_campo12,
    }), required = False)

    nombre_alumno1 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno1 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno1 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno2 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno2 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno2 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno3 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno3 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno3 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno4 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno4 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno4 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno5 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno5 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno5 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno6 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno6 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno6 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno7 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno7 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno7 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno8 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno8 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno8 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno9 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno9 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno9 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno10 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno10 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno10 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno11 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno11 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno11 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno12 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno12 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno12 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno13 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno13 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno13 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno14 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno14 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno14 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno15 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno15 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno15 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno16 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno16 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno16 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno17 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno17 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno17 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno18 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno18 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno18 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno19 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno19 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno19 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno20 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno20 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno20 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno21 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno21 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno21 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno22 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno22 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno22 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno23 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno23 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno23 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno24 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno24 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno24 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno25 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno25 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno25 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno26 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno26 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno26 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno27 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno27 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno27 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno28 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno28 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno28 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno29 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno29 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno29 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno30 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno30 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno30 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno31 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno31 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno31 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno32 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno32 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno32 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno33 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno33 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno33 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno34 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno34 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno34 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno35 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno35 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno35 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno36 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno36 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno36 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno37 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno37 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno37 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno38 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno38 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno38 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno39 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno39 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno39 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nombre_alumno40 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    cedula_alumno40 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    nota_alumno40 = forms.CharField(widget=TextInput(attrs={
    }), required = False)

    
    class Meta:

        model = Planilla
        fields = '__all__'
