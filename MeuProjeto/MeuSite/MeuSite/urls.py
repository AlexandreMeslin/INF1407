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

urlpatterns = [
    path('', include('core.urls')),  # Inclui as URLs da aplicação core para a home-page
    path("admin/", admin.site.urls),
    path('MeuApp/', include('MeuApp.urls')),  # Inclui as URLs da aplicação MeuApp
    path('contatos/', include('contatos.urls')),  # Inclui as URLs da aplicação contatos
    path('contatos-v2/', include('contatos.urls_v2')),  # Inclui as URLs da aplicação contatos
]
