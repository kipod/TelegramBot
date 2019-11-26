from os import path

from .consts import DB_DIR
from .json_db import JsonDb


class User(JsonDb):
    def __init__(self, user_id: int, init_data: dict):
        super().__init__(path.join(DB_DIR, str(user_id), 'user.json'))
        self.uid = user_id
        self.name = init_data.get('name')
        self.surname = init_data.get('surname')
        self.username = init_data.get('username')
        self.work_dir = path.join(DB_DIR, str(user_id))
        self.db = self.load()

    def get_file_by_id(self, file_id: str):
        try:
            return self.db[file_id]
        except KeyError:
            return None

    def add_file(self, file_id, **kwargs):
        file = {}
        self.db[file_id] = file
        for key in kwargs:
            file[key] = kwargs[key]
        self.save(self.db)
