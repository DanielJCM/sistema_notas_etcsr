# -*- coding: utf-8 -*-
from django import forms
from registro.models import Bien
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget

secciones = (
    ('A', 'Seccion A'),
    ('B', 'Seccion B'),
    ('C', 'Seccion C'),
    ('D', 'Seccion D'),
    ('E', 'Seccion E'),
    ('F', 'Seccion F')
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

class BienForm(forms.ModelForm):
    """
    Formulario con los campos de un bien de CENDITEL.
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

    campo2 = forms.CharField(label='Mencion', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo3 = forms.ChoiceField(label='Seccion', widget=Select(attrs={
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

    class Meta:

        model = Bien
        fields = '__all__'
