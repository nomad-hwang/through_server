
from abc import ABC, abstractmethod
from contextlib import asynccontextmanager


class Broker(ABC):
    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    async def publish(self, topic, message, *args, **kwargs):
        pass

    @asynccontextmanager
    @abstractmethod
    async def subscribe(self, topic, *args, **kwargs):
        pass
