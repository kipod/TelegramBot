from os import path

from .consts import DB_DIR
from .json_db import JsonDb
from .user import User


class Users(JsonDb):
    USERS_DB_FILE = path.join(DB_DIR, 'users.json')

    def __init__(self):
        super().__init__(self.USERS_DB_FILE)
        self.users = self.load()

    def __getitem__(self, key):
        if isinstance(key, int):
            data = self.users[key]
            if data:
                return User(key, data)
        return None

    def add_user(self, uid, **kwargs):
        user = {}
        self.users[uid] = user
        for key in kwargs:
            user[key] = kwargs[key]
        self.save(self.users)


users = Users()
