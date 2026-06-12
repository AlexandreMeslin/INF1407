from django.urls import path
from MeuApp import views

app_name = 'MeuApp'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('SegundaPagina/', views.segundaPagina, name='segunda'),
]