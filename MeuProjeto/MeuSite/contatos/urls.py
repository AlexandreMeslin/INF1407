from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    # Adicione suas URLs aqui
    path('', views.ContatoListView.as_view(), name='home-contatos'),
    path('lista/', views.ContatoListView.as_view(), name='lista-contatos'),
]
