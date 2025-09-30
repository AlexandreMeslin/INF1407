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
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.urls.base import reverse_lazy

urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path("contatos/", include('contatos.urls')),
    path("", views.home, name='home'),
    path("formulario/", views.exemplo_form, name='formulario'),
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
    path('seguranca/editarPerfil/<int:pk>', 
        UpdateView.as_view(
            template_name='seguranca/user_form.html',
            model=User,
            fields=['first_name', 'last_name', 'email'],
            success_url=reverse_lazy('sec-home')
        ), 
        name='sec-editar-perfil',
    ),
    # links para resetar senha
    path('seguranca/password_reset/', 
        PasswordResetView.as_view(
            template_name='seguranca/password_reset_form.html',
            email_template_name='seguranca/password_reset_email.html',
            subject_template_name='seguranca/password_reset_subject.html',
            success_url=reverse_lazy('sec-password-reset-done'),
        ),
        name='sec-password-reset'
    ),
    path('seguranca/password_reset_done/',
         PasswordResetDoneView.as_view(
            template_name='seguranca/password_reset_done.html'
         ),
            name='sec-password-reset-done'
    ),
    path('seguranca/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name='seguranca/password_reset_confirm.html',
            success_url=reverse_lazy('sec-password-reset-complete'),
         ),
         name='sec-password-reset-confirm'
    ),
    path('seguranca/password_reset_complete/',
         PasswordResetCompleteView.as_view(
            template_name='seguranca/password_reset_complete.html'
         ),
         name='sec-password-reset-complete'
    ),
]
