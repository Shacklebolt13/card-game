from src.common import consumer as consumer_commons
from src.core import exceptions as commons_exceptions


class EchoConsumer(consumer_commons.Consumer):
    
    @consumer_commons.route("echo")
    async def echo(self, content, **kwargs):
        self.log.info(f"Echo: {content} {kwargs}")
        return {"message": content.get("message", "")}
    