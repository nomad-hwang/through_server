import asyncio

from loguru import logger
from config import load_config

from message.mqtt import Mqtt

async def test_routine(mqtt: Mqtt, topic):
    async for msg in mqtt.subscribe(topic):
        logger.debug(f'{topic} : {msg["payload"]}')
        #await mqtt.publish(topic, msg["payload"])
        #await asyncio.sleep(2) # go easy

async def main():
    conf = load_config('./config/config.yml')    

    mqtt = Mqtt(conf.MQTT.HOST, conf.MQTT.PORT)
    await mqtt.connect()

    asyncio.create_task(test_routine(mqtt, '#'))

    while True:
        await asyncio.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())