# """
# ASGI config for terminal_chat project.

# It exposes the ASGI callable as a module-level variable named ``application``.

# For more information on this file, see
# https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
# """


# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terminal_chat.settings')
# import django

# django.setup()


# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AuthMiddlewareStack(
#         URLRouter(
#             chat.routing.websocket_urlpatterns
#         )
#     )
# })

import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'terminal_chat.settings')
django.setup()
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import chat.routing
from channels.auth import AuthMiddlewareStack
# from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter


# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    )
    # Just HTTP for now. (We can add other protocols later.)
})
