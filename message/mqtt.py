from asyncio.log import logger
from contextlib import asynccontextmanager
from message import Message
from asyncio_mqtt import Client, MqttError

from util.util import replace_params

#  qos: 0: at most once, 1: at least once, 2: exactly once
PUB_DEFAULT = {
    'qos':          1,
    'timeout':      10,
    'retain':       False,
    'properties':   None
}

SUB_DEFAULT = {
    'qos':          0,
    'options':      None,
    'properties':   None
}

class Mqtt(Message, Client):
    def __init__(self, host, port=1883, username=None, password=None) -> None:
        Message.__init__(self)
        Client.__init__(self, host, port, username=username, password=password)
        
        self._status = False

    @property
    def connected(self):
        return self._status

    async def connect(self):
        await Client.connect(self)
        self._status = True

    async def disconnect(self):
        await Client.disconnect(self)
        self._status = False

    async def publish(self, topic, message, *args, **kwargs):
        await Client.publish(self, topic, message, **replace_params(PUB_DEFAULT, **kwargs))

    async def subscribe(self, topic, *args, **kwargs):
        await Client.subscribe(self, topic, **replace_params(SUB_DEFAULT, **kwargs))

        """
        topic :     String. topic that the message was published on.
        payload :   Bytes/Byte array. the message payload.
        qos :       Integer. The message Quality of Service 0, 1 or 2.
        retain :    Boolean. If true, the message is a retained message and not fresh.
        mid :       Integer. The message id.
        properties: Properties class. In MQTT v5.0, the properties associated with the message.
        """
        # TODO Wrap around try except and reconnect if occurs
        async with self.filtered_messages(topic) as msg:
            async for m in msg:
                yield {'topic': m.topic, 'payload': m.payload, 'retain': m.retain, 'timestamp': m.timestamp, 'qos': m.qos}

#class Mqtt(Message, Client):
#    def __init__(self, host, port=1883, username=None, password=None) -> None:
#        Message.__init__(self)
#        Client.__init__(self, host, port, username=username, password=password)

#        self._connected = False # TODO: Find another way to check connection

#    @property
#    def connected(self):
#        return self._connected

#    async def connect(self):
#        await Client.connect(self)

#    async def disconnect(self):
#        await Client.disconnect(self)

#    async def publish(self, topic, message, *args, **kwargs):
#        await Client.publish(self, topic, message, **replace_params(PUB_DEFAULT, **kwargs))

#    async def subscribe(self, topic, *args, **kwargs):
#        await Client.subscribe(self, topic, **replace_params(SUB_DEFAULT, **kwargs))

#        """
#        topic :     String. topic that the message was published on.
#        payload :   Bytes/Byte array. the message payload.
#        qos :       Integer. The message Quality of Service 0, 1 or 2.
#        retain :    Boolean. If true, the message is a retained message and not fresh.
#        mid :       Integer. The message id.
#        properties: Properties class. In MQTT v5.0, the properties associated with the message.
#        """
#        # TODO Wrap around try except and reconnect if occurs
#        async with Client.filtered_messages(self, topic) as msg:
#            async for m in msg:
#                if m.topic == topic:
#                    yield { 'topic': m.topic, 
#                            'payload': m.payload, 
#                            'retain': m.retain, 
#                            'timestamp': m.timestamp, 
#                            'qos': m.qos }

