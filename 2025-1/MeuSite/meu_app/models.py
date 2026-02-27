from django.db import models

# Create your models here.

# meu_app/models.py
from django.db import models
from django.contrib.auth.models import User
import pyotp

class TwoFactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secret = models.CharField(max_length=32, default=pyotp.random_base32)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return f"2FA for {self.user.username}"
    