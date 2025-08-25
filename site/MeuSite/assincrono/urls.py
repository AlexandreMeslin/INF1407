from django.urls import path
from assincrono import views

app_name = 'assincrono'

urlpatterns = [
    path("notificacoes/", views.sse_view, name="sse_notificacoes"),
] 
