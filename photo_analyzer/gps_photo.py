from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim
from bot.consts import DB_DIR
import os
from bot.parser.photo import Photo


class GPSTag(Photo):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def get_gps_tag(usr, file_path):
        photo_path = os.path.join(DB_DIR, usr.uid, file_path)
        coordinates = gpsphoto.getGPSData(photo_path)
        return coordinates

    @staticmethod
    def convert_to_address(coordinates):
        latitude = coordinates.latitude
        longitude = coordinates.longitude
        geographic_locator = Nominatim(user_agent="Telegram")
        location = geographic_locator.reverse("{} , {}".format(latitude, longitude))
        return location.address
