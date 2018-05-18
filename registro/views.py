# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Planilla
from registro.forms import PlanillaForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.generic import *
from django.core.urlresolvers import *
from django.db.models import Count
from django.template import RequestContext


class Index(TemplateView):
    """
    Plantilla de inicio del sistema
    """
    template_name = "registro/index.html"

##############################
##### Crud de las Planillas #####
##############################

class Consultar_planilla(ListView):
    """
    Clase que permite consultar la lista de las planillas registradas.
    """
    model = Planilla


class Registrar_planilla(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar una planilla en el sistema.
    """
    model = Planilla
    form_class = PlanillaForm
    success_url = reverse_lazy('registro:consultar_planilla')
    success_message = "Se ha registrado con éxito"


class Editar_planilla(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de una planilla.
    """
    model = Planilla
    form_class = PlanillaForm
    success_url = reverse_lazy('registro:consultar_planilla')
    success_message = "Se ha actualizado con éxito"


class Borrar_planilla(SuccessMessageMixin,DeleteView):
    """
    Clase que permite borrar una planilla registrada en el sistema.
    """
    model = Planilla
    success_url = reverse_lazy('registro:consultar_planilla')
    success_message = "Se ha eliminado con éxito"

    def delete(self, request, *args, **kwargs):
        """
        Función que permite mandar un mensaje al
        template cuando se borra una planilla.
        """
        messages.success(self.request, self.success_message)
        return super(Borrar_planilla, self).delete(request, *args, **kwargs)
