# import os

# import django
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.auth import AuthMiddlewareStack

# import chat.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
# django.setup()

# application = ProtocolTypeRouter({
#   "http": AsgiHandler(),
#   "websocket": AuthMiddlewareStack(
#       URLRouter(
#           chat.routing.websocket_urlpattern
#       )
#   )
#   # Just HTTP for now. (We can add other protocols later.)
# })


