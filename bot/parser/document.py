import os
from logger import log
from .message import Message
from bot.consts import DB_DIR


class Document(Message):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        self.check_user(message.from_user)
        document = message.document
        user_id = message.from_user.id
        file_id = document.file_id
        file = self.bot.get_file(file_id)
        if self.check_file(file, user_id, message.content_type):
            self.bot.send_message(message.from_user.id, 'This file already exists')
            return
        full_file_path = os.path.join(DB_DIR, str(user_id), file.file_path)
        log(log.DEBUG, 'save document to %s', full_file_path)
        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)
        with open(full_file_path, 'wb') as f:
            f.write(self.bot.download_file(file.file_path))
        self.bot.send_message(message.from_user.id,
                              'Document Size: {} KB'.format(document.file_size // 1024))
