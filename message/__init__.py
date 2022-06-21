
from abc import ABC, abstractmethod, abstractproperty
from contextlib import asynccontextmanager


class Message(ABC):
    @abstractproperty
    def connected(self):
        pass

    @abstractmethod
    async def connect(self):
        pass

    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    async def publish(self, topic, message, *args, **kwargs):
        pass

    @abstractmethod
    async def subscribe(self, topic, *args, **kwargs):
        pass