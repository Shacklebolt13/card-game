from src.consumers.routing import routes
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator
websocket_application = AllowedHostsOriginValidator(
    AuthMiddlewareStack(routes)
)