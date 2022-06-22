from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/', consumers.AsyncCountingConsumer.as_asgi()),
    path('ws/user/', consumers.AsyncUserCountingConsumer.as_asgi()),
]
