# -*- coding: utf-8 -*-
from django import forms
from registro.models import Bien
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)
from datetime import *
from django.contrib.admin.widgets import AdminDateWidget


date=datetime.today().strftime('%Y-%m-%d')

ano = (
    ('-', '-'),
    ('2016', '2016'),
    ('2017', '2017'),
    ('2018', '2018'),
    ('2019', '2019'),
)


class BienForm(forms.ModelForm):

    campo1 = forms.ChoiceField(label='xxx', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = ano)

    campo2 = forms.ChoiceField(label='xxx', widget=Select(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), choices = ano)

    campo3 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo3,
        }), required = False)

    campo4 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo4,
        }), required = False)

    campo5 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo5,
        }), required = False)

    campo6 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo6,
        }), required = False)

    campo7 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo7,
        }), required = False)

    campo8 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo8,
        }), required = False)

    campo9 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo9,
        }), required = False)

    campo10 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo10,
        }), required = False)

    campo11 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo11,
        }), required = False)

    campo12 = forms.CharField(label='xxx', widget=Textarea(attrs={
            'class':'form-control input-md',
            'style': 'min-width: 0; width: 100%; display: inline;',
            #'placeholder': des_campo12,
        }), required = False)

    class Meta:

        model = Bien
        fields = '__all__'
