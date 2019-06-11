from configparser import ConfigParser
from utils.utils import get_app_resources_path
import argparse
import logging

logger = logging.getLogger(__name__)


class Config(object):
    def __init__(self):
        self.config = self.load_config()

    def load_config(self):
        # check if script environment is valid or not
        config = ConfigParser()
        try:
            config_file_path = get_app_resources_path().joinpath("config.properties")
            configuration = config.read(config_file_path)

        except Exception as ex:
            error_message = getattr(ex,'message',str(ex))
            logger.error("Error while reading config.properties - %s",error_message)
            raise ex
        return config
