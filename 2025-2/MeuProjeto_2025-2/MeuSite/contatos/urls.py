from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='home-contatos'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contato'),
    #path('editar/<int:id>/', views.editar_contato, name='editar'),
    #path('remover/<int:id>/', views.deletar_contato, name='remover'),
]
