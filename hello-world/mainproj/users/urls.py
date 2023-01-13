from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.profiles, name='profiles'),
    path('login/', views.LoginPage, name='login'),
]