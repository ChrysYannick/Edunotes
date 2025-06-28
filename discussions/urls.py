from django.urls import path
from . import views

urlpatterns = [
    path('', views.discussion_list, name='discussion_list'),  # Route pour afficher la liste des discussions
    path('create/', views.create_discussion, name='create_discussion'),  # Route pour créer une nouvelle discussion
    path('<int:id>/', views.view_discussion, name='view_discussion'),  # Route pour voir une discussion spécifique
]
