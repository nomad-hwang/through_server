import asyncio

from loguru import logger
from config import load_config

from message.mqtt import Mqtt

async def test_routine(mqtt: Mqtt, topic):
    async for msg in mqtt.subscribe(topic):
        logger.debug(f'publishing {msg["payload"]} to {topic}')
        await mqtt.publish(topic, msg["payload"])
        await asyncio.sleep(2) # go easy

async def main():
    conf = load_config('./config/config.yml')    

    # session = MessageSession(Mqtt(conf.MQTT.HOST, conf.MQTT.PORT))
    mqtt = Mqtt('broker.hivemq.com')
    await mqtt.connect()

    asyncio.create_task(test_routine(mqtt, 'testtopic/1'))
    asyncio.create_task(test_routine(mqtt, 'testtopic/2'))
    asyncio.create_task(test_routine(mqtt, 'testtopic/3'))

    while True:
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())