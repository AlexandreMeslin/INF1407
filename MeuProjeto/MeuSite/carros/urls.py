from django.urls import path
from carros import views

app_name = 'carros'

urlpatterns = [
    path('lista/', views.CarsView.as_view(), name='lista-carros'),
]
