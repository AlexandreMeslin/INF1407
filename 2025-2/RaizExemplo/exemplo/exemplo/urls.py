"""
URL configuration for exemplo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from exemplo import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
from django.urls.base import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("contatos/", include('contatos.urls')),
    path("", views.home, name='home'),
    # links para segurança
    path("seguranca/", views.homeSec, name='sec-home'),
    path("seguranca/registro/", views.registro, name='sec-registro'),
    path("seguranca/login/", 
         LoginView.as_view(template_name='seguranca/login.html'), 
         name='sec-login'),
    path('accounts/login/', 
         LoginView.as_view(template_name='seguranca/login.html'), 
         name='sec-login'),
    # link para página secreta
    path('seguranca/paginaSecreta/', views.paginaSecreta, name='sec-paginaSecreta'),
    # link para confirmar logout
    path('meulogout/', views.logout, name='sec-meulogout'),
    # link para efetuar logout
    path('seguranca/logout/', 
         LogoutView.as_view(next_page=reverse_lazy('sec-home')), 
         name='sec-logout'),
    # links para alterar senha
    path('seguranca/password_change/',
         PasswordChangeView.as_view(
             template_name='seguranca/password_change_form.html',
             success_url=reverse_lazy('sec-password-change-done'),
         ), 
         name='sec-password-change'
    ),
    path('seguranca/password_change_done/', 
         PasswordChangeDoneView.as_view(
             template_name='seguranca/password_change_done.html'
         ), 
         name='sec-password-change-done'
    ),
]
