"""
ASGI config for Edunotes project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing  # Importer le fichier de routage WebSocket de l'app 'chat'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Edunotes.settings')

# L'application ASGI inclut le support WebSocket avec Django Channels
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Gère les requêtes HTTP classiques
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # Routes WebSocket définies dans l'app chat
        )
    ),
})
