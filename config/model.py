from pydantic import BaseSettings

class MqttConfigModel(BaseSettings):
    HOST: str
    PORT: int
    
class ConfigModel(BaseSettings):
    ENV: str
    
    MQTT: MqttConfigModel
