from django.urls import path
from . import views

urlpatterns = [
    path('<str:room_name>/', views.discussion_room, name='discussion_room'),
]
