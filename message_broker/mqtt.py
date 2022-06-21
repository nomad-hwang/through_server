from message_broker import Broker
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

class Mqtt(Broker, Client):
    def __init__(self, host, port=1883, username=None, password=None) -> None:
        Broker.__init__(self)
        Client.__init__(self, host, port, username=username, password=password)

    async def connect(self):
        await Client.connect(self)
    
    async def disconnect(self):
        await Client.disconnect(self)

    async def publish(self, topic, message, *args, **kwargs):
        await Client.publish(topic, message, **replace_params(PUB_DEFAULT, **kwargs))

    async def subscribe(self, topic, *args, **kwargs):
        await Client.subscribe(topic, **replace_params(SUB_DEFAULT, **kwargs))

    
