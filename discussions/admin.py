from django.contrib import admin
from .models import Comment

# Register your models here.
admin.site.register(Comment)

class CommentAdmin(admin.ModelAdmin):
     list_display=('document', 'user', 'content', 'created_at')
     search_fields = ('user', 'document')
     list_filter = ('created_at',)