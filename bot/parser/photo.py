from .message import Message
from photo_analyzer.gps_photo import GPSTag


class Photo(Message):

    def __init__(self, gps=GPSTag, *args, **kwargs):
        self.__gps = gps
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

    def get_coordinates(self, message):
        file = self.bot.get_file(message.photo[-1].file_id)
        coordinates = self.__gps.get_gps_tag(self.users.get_user(message.from_user), file.file_path)
        if coordinates.latitude is None or coordinates.longitude is None:
            self.bot.send_message(message.from_user.id, 'This photo has not got GPS tag')
            return
        try:
            address = self.__gps.convert_to_address(coordinates)
            self.bot.send_message(message.from_user.id, 'This photo was taken by this address : {}'.format(address))
        except Exception:
            self.bot.send_message(message.from_user.id, 'Unable to take address from this photo')
