# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from registro.models import Planilla, Bitacora
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
from datetime import datetime

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

    def get(self, request, *args, **kwargs):
        """
        Método que muestra cual usuario y cuando visito la lista de personas.
        """
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.")
                          % {'class_name': self.__class__.__name__})
        context = self.get_context_data(object_list=self.object_list)
        #print "***** El usuario: "+str(self.request.user)+", visito la lista de personas el: "+str(datetime.now())+" *****"
        #a = "El usuario: "+str(self.request.user)+", visito la lista de personas el: "+str(datetime.now())
        #Bitacora.objects.create(entrada=a)
        return self.render_to_response(context)


class Registrar_planilla(SuccessMessageMixin,CreateView):
    """
    Clase que permite registrar una planilla en el sistema.
    """
    model = Planilla
    form_class = PlanillaForm
    success_url = reverse_lazy('registro:consultar_planilla')
    success_message = "Se ha registrado con éxito"

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando registro a una persona y lo guarda en la tabla bitacora
        """
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")

        self.object = form.save()
        #print "***** El usuario: "+str(self.request.user)+", registro una persona el: "+str(datetime.now())+" *****"
        a = "El usuario: "+str(self.request.user)+", registro una planilla el: "+str(formatedDate)
        Bitacora.objects.create(usuario=a)
        return super(Registrar_planilla, self).form_valid(form)


class Editar_planilla(SuccessMessageMixin,UpdateView):
    """
    Clase que permite editar la data guardada de una planilla.
    """
    model = Planilla
    form_class = PlanillaForm
    success_url = reverse_lazy('registro:consultar_planilla')
    success_message = "Se ha actualizado con éxito"

    def form_valid(self, form):
        """
        Método que muestra cual usuario y cuando actualizo a una persona y lo guarda en la tabla bitacora
        """
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")

        self.object = form.save()
        #print "***** El usuario: "+str(self.request.user)+", actualizo una persona el: "+str(datetime.now())+" *****"
        a = "El usuario: "+str(self.request.user)+", actualizó una planilla el: "+str(formatedDate)
        Bitacora.objects.create(usuario=a)
        return super(Editar_planilla, self).form_valid(form)

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
        myDate = datetime.now()
        formatedDate = myDate.strftime("%d-%m-%Y %H:%M")

        messages.success(self.request, self.success_message)
        a = "El usuario: "+str(self.request.user)+", elimino una planilla"
        b = str(formatedDate)
        Bitacora.objects.create(accion=a)
        Bitacora.objects.create(fecha=b)
        return super(Borrar_planilla, self).delete(self, request, *args, **kwargs)


class BitacoraView(ListView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Bitacora
    template_name = "registro/bitacora.html"

    def get_queryset(self):
        """
        Método que filtra los datos de la tabla, solo muestra si coincide con el filtro
        """
        #queryset = Bitacora.objects.filter(tipo='Actualización')
        queryset = Bitacora.objects.order_by('-id')
        return queryset