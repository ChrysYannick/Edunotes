from django.db import models
from django.conf import settings
from users.models import CustomUser

class Document(models.Model):
    TYPE_CHOICES = (
        ("course", "Cours"),
        ("assignment", "Devoir"),
        ("exam", "Examen"),
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="documents/") 
    doc_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_doc_type_display()})"
    

# fonction permettant de telecharger un document selon l'utilisateur connecté
# j'utilises un modèle personnalisé pour l’utilisateur (CustomUser), donc je dois utilisé 
#from django.contrib.auth.models import User
#user = models.ForeignKey(User, on_delete=models.CASCADE)
 
class Download(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    downloaded_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        unique_together = ('user', 'document')  # Empêche les doublons

    def __str__(self):
        return f"{self.user.username} a téléchargé {self.document.title}"