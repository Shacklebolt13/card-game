from typing import Any, Callable, Dict,Coroutine
from abc import ABCMeta
from channels.generic.websocket import AsyncJsonWebsocketConsumer  # type: ignore
from ..core.logging import logger
from logging import Logger

ROUTING_TABLE : Dict[str, Callable] = {}

def route(handler : str) -> Callable:
    def decorator(func : Callable) -> Callable:
        ROUTING_TABLE[handler] = func
        return func
    return decorator

@logger
class Consumer(AsyncJsonWebsocketConsumer,metaclass=ABCMeta):
    log : Logger
    
    @property
    def get_routing(self) -> Dict[str, Callable]:
        return ROUTING_TABLE

    AUTH = False

    async def connect(self):
        await super().connect()

        user = self.scope.get("user",None)
        user = user.is_authenticated or None

        if self.AUTH and not user:
            await self.send_json({"message": "unauthorized"})
            return await self.close()

        return await self.send_json(
            {
                "message": "connected",
                "user": str(user),
            }
        )

    async def handle(self, content: Dict[str, Any], **kwargs) -> Dict:
        """
        Handle incoming messages and route them to the appropriate handler.
        """
        handler = self.get_routing.get(content.get("handler", ""), Consumer.no_route)
        return await handler(self, content, **kwargs)

    async def no_route(self, content, **kwargs) -> Dict:
        return {"message": f"No route for {content.get('handler', '')}"}

    async def receive_json(self, content, **kwargs) -> None:
        return await self.send_json(await self.handle(content, **kwargs), **kwargs)
