import os
from logger import log
from .consts import DB_DIR
from .json_db import JsonDb


class User(JsonDb):
    def __init__(self, user_id: str, init_data: dict):
        super().__init__(os.path.join(DB_DIR, user_id, 'user.json'))
        self.uid = user_id
        self.name = init_data.get('name')
        self.surname = init_data.get('surname')
        self.username = init_data.get('username')
        self.work_dir = os.path.join(DB_DIR, user_id)
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

    def download_file(self, file_id, content_type, bot):
        file = bot.get_file(file_id)
        full_file_path = os.path.join(self.work_dir, file.file_path)
        log(log.DEBUG, 'save photo to %s', full_file_path)
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
        with open(full_file_path, 'wb') as f:
            f.write(bot.download_file(file.file_path))
        self.add_file(file_id=file_id, content_type=content_type, file_path=full_file_path)

    def check_file(self, file_id):
        return True if self.get_file_by_id(file_id) else False
