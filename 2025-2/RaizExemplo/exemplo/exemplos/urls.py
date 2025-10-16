from django.urls import path
from exemplos import views

app_name = 'exemplos'

urlpatterns = [
    path('exemploClasse/', views.ExemploClasse.as_view(), name='exemploClasse'),
    path('exemploGet/', views.exemploGet, name='exemploGet'),
    path('exemploPost/', views.exemploPost, name='exemploPost'),
    path('exemploPutDelete/', views.exemploPutDelete, name='exemploPutDelete'),
]
