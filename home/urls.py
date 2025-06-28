from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Route vers la page d'accueil
]
