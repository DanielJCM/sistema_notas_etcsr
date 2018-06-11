# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from registro import views
from registro.views import *
import registro.views as views
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
    #url(r'^index$', login_required(Index.as_view()), name='index'),
    #url(r'^consultar_bien$', login_required(views.Consultar_bien.as_view()), name='consultar_bien'),
    #url(r'^registrar_bien$', login_required(views.Registrar_bien.as_view()), name='registrar_bien'),
    #url(r'^editar_bien/(?P<pk>\d+)$', login_required(views.Editar_bien.as_view()), name='editar_bien'),
    #url(r'^borrar_bien/(?P<pk>\d+)$', login_required(views.Borrar_bien.as_view()), name='borrar_bien'),
    url(r'^index$', login_required(Index.as_view()), name='index'),
    url(r'^consultar_planilla$', login_required(views.Consultar_planilla.as_view()), name='consultar_planilla'),
    url(r'^registrar_planilla$', login_required(views.Registrar_planilla.as_view()), name='registrar_planilla'),
    url(r'^editar_planilla/(?P<pk>\d+)$', login_required(views.Editar_planilla.as_view()), name='editar_planilla'),
    url(r'^ver_planilla/(?P<pk>\d+)$', login_required(views.Ver_planilla.as_view()), name='ver_planilla'),
    url(r'^borrar_planilla/(?P<pk>\d+)$', login_required(views.Borrar_planilla.as_view()), name='borrar_planilla'),
    url(r'^bitacora', login_required(views.BitacoraView.as_view()), name='bitacora'),
)
