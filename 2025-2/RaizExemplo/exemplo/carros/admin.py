from django.contrib import admin

# Register your models here.

from carros.models import MTCars

# Registrando o modelo MTCars na
# interface de administração do Django
admin.site.register(MTCars)
