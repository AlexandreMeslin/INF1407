"""
URL configuration for MeuSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import include
from MeuSite import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordChangeDoneView
#from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from MeuSite.views import MeuUpdateView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularSwaggerView
from drf_spectacular.views import SpectacularRedocView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

app_name = 'MeuSite'

#schema_view = get_schema_view(
#    title="API de Carros",
#    description="Documentação OpenAPI da API de carros",
#    version="1.0.0",
#    url="https://supreme-space-guacamole-5vpvp7vw5q627p6-8000.app.github.dev/",
#)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home, name='home'),
    path("MeuApp/", include("MeuApp.urls")),
    path("contatos/", include("contatos.urls")),
    # Segurança
    path("seguranca/", views.homeSec, name='sec-home'),
    path("seguranca/registro/", views.registro, name='sec-registro'),
    path("seguranca/login/", LoginView.as_view(template_name='seguranca/login.html'), name='sec-login'),
    path('seguranca/profile/', views.paginaSecreta, name='sec-paginaSecreta'),
    path('meulogout/', views.logout, name='sec-meulogout'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('sec-home')), name='sec-logout'),
    path('seguranca/password_change/', 
        PasswordChangeView.as_view(
            template_name='seguranca/password_change_form.html', 
            success_url=reverse_lazy('sec-password_change_done'),
        ), name='sec-password_change'),
    path('seguranca/password_change_done/',
        PasswordChangeDoneView.as_view(
            template_name='seguranca/password_change_done.html'),
        name='sec-password_change_done'),
    path('seguranca/atualiza_usuario/<int:pk>/',
        MeuUpdateView.as_view(
            model=User,
            fields=[
                'first_name',
                'last_name',
                'username', 
                'email',
            ],
            template_name='seguranca/user_form.html',
            success_url=reverse_lazy('sec-home')
        ), name='sec-atualiza_usuario'),
    path('seguranca/password_reset/',
        PasswordResetView.as_view(
            template_name='seguranca/password_reset_form.html',
            email_template_name='seguranca/password_reset_email.html',
            success_url=reverse_lazy('sec-password_reset_done'),
            html_email_template_name='seguranca/password_reset_email.html',
            subject_template_name='seguranca/password_reset_subject.txt',
            from_email='webmaster@meslin.com.br',
        ), name='sec-password_reset'),
    path('seguranca/password_reset_done/',
        PasswordResetDoneView.as_view(
            template_name='seguranca/password_reset_done.html'),
        name='sec-password_reset_done'),
    path('seguranca/password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='seguranca/password_reset_confirm.html',
            success_url=reverse_lazy('sec-password_reset_complete'),
        ), name='sec-password_reset_confirm'),
    path('seguranca/password_reset_complete/',
        PasswordResetCompleteView.as_view(
            template_name='seguranca/password_reset_complete.html'),
        name='sec-password_reset_complete'),
    path("carros/", include("carros.urls")),

    # Schema OpenAPI JSON
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger-ui'),
    # ReDoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema-redoc'),
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
