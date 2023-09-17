from .echo_consumer import EchoConsumer
from django.urls import path
from channels.routing import URLRouter # type: ignore

routes = URLRouter([
    path("echo",EchoConsumer.as_asgi(), name="echo")
])
