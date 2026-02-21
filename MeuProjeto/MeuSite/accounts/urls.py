from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('whoami/', views.whoami, name='whoami'),
    path('change-password/', views.CustomAuthToken.as_view(), name='change_password'),
    path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
]
