from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', include('documents.urls')),
    path('users/', include('users.urls')),
    path('discussions/', include('chats.urls')),
    path('', include('home.urls')),  # Page d'accueil

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
