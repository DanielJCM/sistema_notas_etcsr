# -*- coding: utf-8 -*-
from django import forms
from registro.models import Bien
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget


date=datetime.today().strftime('%Y-%m-%d')

sit_jur = (
    ('-', '-'),
    ('Propio', 'Propio'),
    ('Comodato', 'Comodato'),
    ('Préstamo', 'Préstamo'),
)

"""
Capcidad del disco duro
Memoria RAM instalada
Version del Sistema Operativo Instalado.
Arquitectura del procesador usada por el SO.
"""

class BienForm(forms.ModelForm):

    campo0 = forms.CharField(label='Asignado a', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo1 = forms.CharField(label='Código de inventario del Bien', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo2 = forms.CharField(label='Número de puesto asignado al Bien', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo4,
    }), required = False)

    campo3 = forms.ChoiceField(label='Situación Jurídica del Bien', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = sit_jur)

    campo4 = forms.CharField(label='Descripción del bien', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo3,
    }), required = False)

    campo5 = forms.CharField(label='Marca', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo5,
    }), required = False)

    campo6 = forms.CharField(label='Modelo', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo6,
    }), required = False)

    campo7 = forms.CharField(label='Serial', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo7,
    }), required = False)

    campo8 = forms.CharField(label='Color', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo8,
    }), required = False)

    campo9 = forms.CharField(label='Estado', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo9,
    }), required = False)

    campo10 = forms.CharField(label='Año', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo10,
    }), required = False)

    campo11 = forms.CharField(label='Observaciones', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo11,
    }), required = False)

    campo12 = forms.CharField(label='Características Técnicas', widget=Textarea(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        #'placeholder': des_campo12,
    }), required = False)

    class Meta:

        model = Bien
        fields = '__all__'
