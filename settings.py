from dotenv import dotenv_values
import os


class Dotenv:
    """Loads .env file"""

    file_path = ".env"

    @classmethod
    def get_config(cls):
        if not os.path.exists(cls.file_path):
            raise FileNotFoundError(".env file not found in project root. Create it and store your API key to api_key")
        else:
            return dotenv_values(cls.file_path)


class DataInDotEnv:
    """Designed to retrieve datas from .env by provided key"""
    dotenv_config = Dotenv.get_config()

    @classmethod
    def get_value(cls, dict_key):
        return cls.dotenv_config.get(dict_key, None)


class ApiToken:
    __dict_key = "api_key"

    @classmethod
    def reveal_token(cls):
        api_key = DataInDotEnv.get_value(cls.__dict_key)
        return api_key
