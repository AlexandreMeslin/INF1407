from django.urls import path

from contatos import views_v2 as views

app_name = 'contatos-v2'

urlpatterns = [
    path('', views.ContatoListView.as_view(), name='home-contatos'),
    path('listar/', views.ContatoListView.as_view(), name='listar-contatos'),
    path('criar/', views.ContatoCreateView.as_view(), name='criar-contato'),
    path('apagar/<int:pk>/', views.ContatoDeleteView.as_view(), name='apagar-contato'),
    path('atualizar/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualizar-contato'),
]