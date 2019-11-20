import os
from logger import log
from .message import Message
from bot.users import users


class Photo(Message):
    ROOT_FOLDER = 'db'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        assert isinstance(message.photo, list)
        self.__check_user(message.from_user)
        photo = message.photo[-1]
        user_id = message.from_user.id
        file_id = photo.file_id
        file = self.bot.get_file(file_id)
        full_file_path = os.path.join(self.ROOT_FOLDER, str(user_id), file.file_path)
        log(log.DEBUG, 'save photo to %s', full_file_path)
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
        # TODO: if file full_file_path already exists don't download it again
        with open(full_file_path, 'wb') as f:
            f.write(self.bot.download_file(file.file_path))
        self.bot.send_message(message.from_user.id,
                              'Photo Size: {}x{} Total: {} KB'.format(photo.height,
                                                                      photo.width, photo.file_size // 1024))

    @staticmethod
    def __check_user(user):
        u = users[user.id]
        if not u:
            users.add_user(uid=user.id, name=user.first_name, surname=user.last_name, username=user.username)
