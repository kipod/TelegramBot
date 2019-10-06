import os
import json
CONFIG_FILE_NAME = 'bot.conf'


class Configuration(object):
    def __init__(self):
        self.__bot_token = None
        self.__bot_manager_token = None
        if not os.path.exists(CONFIG_FILE_NAME):
            return
        with open(CONFIG_FILE_NAME, 'r') as file:
            json_obj = json.loads(str.join('\n', file.readlines()))
            self.__bot_token = json_obj['bot_token'] \
                if 'bot_token' in json_obj else None
            self.__bot_manager_token = json_obj['bot_manager_token'] \
                if 'bot_manager_token' in json_obj else None

    @property
    def bot_token(self):
        return self.__bot_token

    @property
    def bot_manager_token(self):
        return self.__bot_manager_token


CONFIG = Configuration()
