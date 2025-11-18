from carros import views
from django.urls import path

app_name = 'carros'

urlpatterns = [
    path('lista/', views.CarsView.as_view(), name='lista-carros'),
    path('umcarro/', views.CarView.as_view(), name='um-carro'),
]