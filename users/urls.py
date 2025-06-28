from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
     path('register/', views.register, name='register'),  # Route pour l'inscription
     path('login/', views.user_login, name='login'),      # Route pour la connexion
     path('logout/', views.user_logout, name='logout'),      # Route pour la connexion
     
     path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
]
