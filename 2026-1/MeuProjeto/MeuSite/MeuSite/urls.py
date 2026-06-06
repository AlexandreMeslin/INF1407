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

# Para o Swagger
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.views import SpectacularRedocView
from drf_spectacular.views import SpectacularSwaggerView

# Para o JWT
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("meuapp/", include("MeuApp.urls")),
    path("", include("portal.urls")),
    path("contatos/", include("contatos.urls")),
    path("carros/", include("carros.urls")),
    # Rotas para o Swagger
    path('api/schema/', SpectacularAPIView.as_view(authentication_classes=[], permission_classes=[AllowAny],), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema', authentication_classes=[], permission_classes=[AllowAny],), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema', authentication_classes=[], permission_classes=[AllowAny],), name='redoc-ui'),
    # Rotas para o JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('accounts/', include('accounts.urls')),
]
