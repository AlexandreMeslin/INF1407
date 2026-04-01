from django.urls import path
from contatos import views

app_name = 'contatos'

urlpatterns = [
    # Adicione suas URLs aqui
    path('', views.ContatosListView.as_view(), name='home-contatos'),
    path('lista/', views.ContatosListView.as_view(), name='lista-contatos'),
    path('detalhes/<int:pk>/', views.ContatoDetailView.as_view(), name='detalhes-contato'),
    path('cria/', views.ContatoCreateView.as_view(), name='cria-contato'),
    path('atualiza/<int:pk>/', views.ContatoUpdateView.as_view(), name='atualiza-contato'),
    path('apaga/<int:pk>/', views.ContatoDeleteView.as_view(), name='apaga-contato'),
    path("toggle-theme/", views.toggle_theme, name="toggle-theme"),
]

