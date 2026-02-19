from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('whoiam/', views.whoiam, name='whoiam'),
    path('change-password/', views.CustomAuthToken.as_view(), name='change_password'),
]
