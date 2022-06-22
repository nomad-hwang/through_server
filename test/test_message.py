import asyncio
import unittest
from message.error import NoConnection

from message.mock import MockEcho
from message.mqtt import Mqtt

class TestWithMock(unittest.IsolatedAsyncioTestCase):
    async def test_exception(self):
        intf = MockEcho()
        
        with self.assertRaises(NoConnection):
            await intf.publish('testtopic', 'hello world!')
        
        with self.assertRaises(NoConnection):
            async for msg in intf.subscribe('testtopic'):
                pass

    async def test_pubsub(self):
        intf = MockEcho()
        await intf.connect()

        async def test(cnt):
            topic = f'this/is/sparta/{cnt}'
            payload = f'{300 + cnt}'

            await intf.publish(topic, payload, retain=True)
                    
            async for msg in intf.subscribe(topic):
                self.assertEqual(msg['topic'], topic)
                self.assertEqual(msg['payload'], payload)
                break

        await asyncio.gather(*[test(i) for i in range(100)])
                