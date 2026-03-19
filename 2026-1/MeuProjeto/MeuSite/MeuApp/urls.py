from django.urls import path
from MeuApp import views

app_name = 'MeuApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('segunda-pagina/', 
         views.segundaPagina, 
         name='segunda_pagina'),
]