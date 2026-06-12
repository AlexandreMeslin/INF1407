from django.urls import path

from MeuApp import views

app_name = 'MeuApp'

urlpatterns = [
    path('', views.home, name='homeApp'),
    path('segundaPagina/', views.segundaPagina, name='segunda_pagina'),
]