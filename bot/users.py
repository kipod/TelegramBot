from os import path
import json


class Users(object):
    USERS_DB_FILE = path.join('db', 'users.json')

    def __init__(self):
        self.users = {}
        self.__save()
        self.__load()

    def __getitem__(self, key):
        if isinstance(key, int):
            pass
        else:
            return None

    def __load(self):
        with open(self.USERS_DB_FILE, 'r') as f:
            self.users = json.load(f)

    def __save(self):
        with open(self.USERS_DB_FILE, 'w') as f:
            f.write(json.dumps(self.users, indent=4))

    def add_user(self, uid, **kwargs):
        user = {}
        self.users[uid] = user
        for key in kwargs:
            user[key] = kwargs[key]
        self.__save()


users = Users()
