from django.contrib import admin
from .models import Document

# Register your models here.
admin.site.register(Document)

class DocumentAdmin(admin.ModelAdmin):
     list_display = ('titre', 'description', 'file', 'doc_type', 'uploaded_by', 'uploaded_at')
     search_fields = ('titre', 'description', 'doc_type')
     list_filter = ('titre')