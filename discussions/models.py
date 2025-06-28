from django.db import models
from users.models import CustomUser
from documents.models import Document

class Comment(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user.username} sur {self.document.title}"
