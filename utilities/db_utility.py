from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError
from utilities.config_reader import ConfigReader

class DBManager:
    def __init__(self):
        config = ConfigReader()
        self.host = config.get('database', 'host')
        self.port = config.get('database', 'port')
        self.user = config.get('database', 'user')
        self.password = config.get('database', 'password')
        self.database = config.get('database', 'database')
        self.driver = config.get('database', 'driver')

    def get_connection_string(self) -> str:
        return f"{self.driver}://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    def get_engine(self) -> Engine:
        try:
            connection_string = self.get_connection_string()
            engine = create_engine(connection_string)
            return engine
        except SQLAlchemyError as e:
            raise e
