from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetRoutes),
    path('projects/', views.GetProjects),
    path('projects/<str:pk>', views.GetProject),
]