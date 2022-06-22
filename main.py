import asyncio
import time

from loguru import logger
from config import load_config
from message import Message

from message.mqtt import Mqtt

async def test_routine_sub(message: Message, topic):
    async for msg in message.subscribe(topic):
        logger.debug(f'Received {topic} : {msg["payload"]}')
    print("exit")

async def test_routine_pub(message: Message, topic):
    while True:
        await message.publish(topic, f'{time.time()} lets go')
        await asyncio.sleep(.5)

async def main():
    conf = load_config('./config/config.yml')    

    mqtt = Mqtt(conf.MQTT.HOST, conf.MQTT.PORT)
    await mqtt.connect()

    asyncio.create_task(test_routine_pub(mqtt, 'test/'))
    asyncio.create_task(test_routine_sub(mqtt, 'test/'))

    while True:
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())