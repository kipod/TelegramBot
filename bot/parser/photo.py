import os
from .message import Message


class Photo(Message):
    ROOT_FOLDER = 'db'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        assert isinstance(message.photo, list)
        for photo in message.photo:
            file_id = photo.file_id
            file = self.bot.get_file(file_id)
            full_file_path = os.path.join(self.ROOT_FOLDER, file.file_path)
            os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
            with open(full_file_path, 'wb') as f:
                f.write(self.bot.download_file(file.file_path))
            pass
