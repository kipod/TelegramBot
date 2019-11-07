import os
from .message import Message


class Photo(Message):
    ROOT_FOLDER = 'db'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        assert isinstance(message.photo, list)
        photo = message.photo[-1]
        user_id = str(message.from_user.id)
        file_id = photo.file_id
        file = self.bot.get_file(file_id)
        photo_path = user_id + '/' + file.file_path
        full_file_path = os.path.join(self.ROOT_FOLDER, photo_path)
        if os.path.exists(full_file_path):
            with open(full_file_path, 'wb') as f:
                f.write(self.bot.download_file(file.file_path))
            self.bot.send_message(message.from_user.id,
                                  'Photo Size: {}x{} Total: {} KB'.format(photo.height,
                                                                          photo.width, photo.file_size//1024))
        else:
            os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
            with open(full_file_path, 'wb') as f:
                f.write(self.bot.download_file(file.file_path))
            self.bot.send_message(message.from_user.id,
                                  'Photo Size: {}x{} Total: {} KB'.format(photo.height,
                                                                          photo.width, photo.file_size//1024))
