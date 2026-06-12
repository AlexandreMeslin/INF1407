from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # Rota para a home-page do projeto
]