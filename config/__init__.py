import yaml
from loguru import logger

from config.model import ConfigModel

def load_config(path: str) -> ConfigModel:
    try:
        with open(path, 'r') as f:
            ret = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"config file load fail from {path}. {e}")
        exit(-1)

    return ConfigModel(ENV=ret['ENV'], **ret[ret['ENV']])



