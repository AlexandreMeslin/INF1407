from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class PasswordResetCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    used = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.code}"

    def is_expired(self):
        # Considera o código expirado após 15 minutos
        return timezone.now() > self.created_at + timezone.timedelta(minutes=15)
    