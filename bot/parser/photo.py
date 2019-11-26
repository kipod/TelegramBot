import os
from logger import log
from .message import Message
from bot.users import users
from bot.consts import DB_DIR


class Photo(Message):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        assert isinstance(message.photo, list)
        self.__check_user(message.from_user)
        photo = message.photo[-1]
        user_id = message.from_user.id
        file_id = photo.file_id
        file = self.bot.get_file(file_id)
        if self.__check_file(file, user_id):
            self.bot.send_message(message.from_user.id, 'This file already exists')
            return
        full_file_path = os.path.join(DB_DIR, str(user_id), file.file_path)
        log(log.DEBUG, 'save photo to %s', full_file_path)
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
        with open(full_file_path, 'wb') as f:
            f.write(self.bot.download_file(file.file_path))
        self.bot.send_message(message.from_user.id,
                              'Photo Size: {}x{} Total: {} KB'.format(photo.height,
                                                                      photo.width, photo.file_size // 1024))

    @staticmethod
    def __check_user(user):
        u = users[str(user.id)]
        if not u:
            users.add_user(uid=user.id, name=user.first_name, surname=user.last_name, username=user.username)

    @staticmethod
    def __check_file(file, uid):
        user = users[str(uid)]
        user_file = user.get_file_by_id(file.file_id)
        if not user_file:
            user.add_file(file_id=file.file_id, content_type='photo', file_path=file.file_path)
            return False
        else:
            return True
