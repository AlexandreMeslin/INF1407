from django.urls import path
from . import views

app_name = "meu_app"

urlpatterns = [
    path("2fa/setup/", views.setup_2fa, name="setup_2fa"),
    path("2fa/verify/", views.verify_2fa, name="verify_2fa"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("", views.home, name="home"),
]
