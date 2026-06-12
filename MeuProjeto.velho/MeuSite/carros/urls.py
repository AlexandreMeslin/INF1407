from django.urls import path
from carros import views

app_name = 'carros'

urlpatterns = [
    path('varioscarros/', views.CarsView.as_view(), name='varios-carros'),
    path('criar/', views.CarCreateView.as_view(), name='criar-carro'),
    path('umcarro/<int:pk>/', views.CarView.as_view(), name='um-carro'),
    path('some-protected-view/', views.exemplo_protegido, name='exemplo-protegido'),
]
