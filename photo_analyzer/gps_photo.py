import os
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim
from bot.consts import DB_DIR


class GPSTag(object):

    def __init__(self):
        self.geographic_locator = Nominatim(user_agent="Telegram")

    @staticmethod
    def get_gps_tag(usr, file_path):
        photo_path = os.path.join(DB_DIR, usr.uid, file_path)
        coordinates = gpsphoto.getGPSData(photo_path)
        return coordinates

    def convert_to_address(self, coordinates):
        latitude = coordinates.latitude
        longitude = coordinates.longitude
        location = self.geographic_locator.reverse("{} , {}".format(latitude, longitude))
        return location.address
