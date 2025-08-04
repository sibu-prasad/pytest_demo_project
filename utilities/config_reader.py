import configparser
import os

class ConfigReader:
    _instance = None
    config = None  # Explicitly declare config as an instance variable
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.config = configparser.ConfigParser()
            config_path = os.path.join(os.path.dirname(__file__), '..', 'config.ini')
            cls._instance.config.read(config_path)
        return cls._instance
    
    def get(self, section, option):
        return self.config.get(section, option)