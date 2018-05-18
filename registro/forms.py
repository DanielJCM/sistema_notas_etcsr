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

    class Meta:

        model = Planilla
        fields = '__all__'
