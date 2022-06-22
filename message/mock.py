

import asyncio
from contextlib import asynccontextmanager
import time
from typing import Dict
from message import Message
from message.error import NoConnection

# def check_conn(method):
#     async def method_wrapper(self, *args, **kwargs):
#         if not getattr(self, '_status'):
#             raise NoConnection()            
#         return await method(self, *args, **kwargs)
#     return method_wrapper

class MockEcho(Message):
    def __init__(self) -> None:
        Message.__init__(self)

        self._status = False
        self._q_list: Dict[str, asyncio.Queue] = dict()

    @property
    def connected(self):
        return self._status

    async def connect(self):
        self._status = True

    async def disconnect(self):
        self._status = False

    async def publish(self, topic, message, *args, **kwargs):
        _check_conn(self.connected)
        _check_q_exist(self._q_list, topic)
        
        self._q_list[topic].put_nowait(message)

    async def subscribe(self, topic, *args, **kwargs):
        _check_conn(self.connected)
        _check_q_exist(self._q_list, topic)

        async with _message(self._q_list[topic], topic) as msg:
            async for m in msg:
                yield m

@asynccontextmanager
async def _message(queue: asyncio.Queue, topic):
    async def _generator():
        while True:
            msg = await queue.get()
            yield {'topic': topic, 'payload': msg, 'retain': False, 'timestamp': time.time(), 'qos': 0}
    try:
        yield _generator()
    finally:
        pass

def _check_conn(status):
    if not status:
        raise NoConnection

def _check_q_exist(q_list: dict, topic):
    if topic in q_list:
        return
    q_list[topic] = asyncio.Queue()
