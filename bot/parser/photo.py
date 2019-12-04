from .message import Message


class Photo(Message):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def message(self, message):
        assert isinstance(message.photo, list)
        usr = self.users.get_user(message.from_user)
        photo = message.photo[-1]
        file = self.bot.get_file(photo.file_id)
        if usr.check_file(file.file_id):
            self.bot.send_message(message.from_user.id, 'This file already exists')
            return
        usr.download_file(photo.file_id, message.content_type, self.bot)
        self.bot.send_message(message.from_user.id,
                              'Photo Size: {}x{} Total: {} KB'.format(photo.height,
                                                                      photo.width, photo.file_size // 1024))
