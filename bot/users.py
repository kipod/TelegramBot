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
        user_id = str(key)
        data = self.users[user_id]
        if data:
            return User(user_id, data)
        return None

    def __add_user(self, uid, **kwargs):
        user = {}
        self.users[uid] = user
        for key in kwargs:
            user[key] = kwargs[key]
        self.save(self.users)

    def get_user(self, user):
        usr = self[str(user.id)]
        if not usr:
            self.__add_user(uid=user.id, name=user.first_name, surname=user.last_name, username=user.username)
            usr = self[str(user.id)]
            assert usr
        return usr


users = Users()
