from django.urls import path
from . import views

urlpatterns = [
    # Par exemple, une route pour afficher la liste des documents
    path('cours/', views.cours, name='cours'), 
    path('devoir/', views.devoir, name='devoir'), 
    path('examen/', views.examen, name='examen'), 


    path("etudiant/cours/", views.student_cours, name="student_cours"),
    path("etudiant/devoirs/", views.student_devoirs, name="student_devoirs"),
    path("etudiant/examens/", views.student_examens, name="student_examens"),
    path("etudiant/supprimer/<int:pk>/", views.delete_document, name="delete_document"),

    #urls pour le telechargements des documents
    path('download/<int:doc_id>', views.download_document, name='download_document'),


]