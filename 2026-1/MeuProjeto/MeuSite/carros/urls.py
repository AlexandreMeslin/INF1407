from django.urls import path

from carros import views

app_name = 'carros'

urlpatterns = [
    path('varioscarros/', views.CarsView.as_view(), name='varios-carros'),
]