from django.urls.conf import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('', views.ContatoListView.as_view(), name='home-contatos'),
    path('busca/', views.buscaUmContato, name='busca-contato'),
    path('retorno-busca/', views.respostaBuscaUmContato, name='mostra-contato'),
]
