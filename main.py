import asyncio

from loguru import logger
from config import load_config

from message_broker.mqtt import Mqtt

async def main():
    conf = load_config('./config/config.yml')
    logger.info(f"environment setup: {conf.ENV}")
    
    mqtt = Mqtt(conf.MQTT.HOST, conf.MQTT.PORT)
    await mqtt.connect()
    await mqtt.publish('testtopic/1', 'ㅇㅅㅇㅅㅇㅅㅇ')

    while True:
        await asyncio.sleep(0.1)
    

if __name__ == "__main__":
    asyncio.run(main())