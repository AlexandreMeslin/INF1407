from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import TwoFactor

@admin.register(TwoFactor)
class TwoFactorAdmin(admin.ModelAdmin):
    list_display = ("user", "enabled")
    