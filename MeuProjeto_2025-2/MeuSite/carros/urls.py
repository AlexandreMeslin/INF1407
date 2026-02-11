from django.urls import path
from carros import views

app_name = 'carros'

urlpatterns = [
    path("lista/", views.CarsView.as_view(), name='lista-carros'),
    path('umcarro/', views.CarView.as_view(), name='um-carro'),
    path('umcarro/<int:id_arg>/', views.CarView.as_view(), name='consulta-carro'),
]
