import yaml
from loguru import logger

from config.model import ConfigModel

def load_config(path: str) -> ConfigModel:
    try:
        with open(path, 'r') as f:
            ret = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed loading config file from {path}")
        logger.error(e)
        exit(-1)
    
    logger.info(f"CONFIG ENV: {ret['ENV']}")
    return ConfigModel(ENV=ret['ENV'], **ret[ret['ENV']])



