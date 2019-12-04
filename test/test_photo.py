from bot.parser import Photo
TEST_USER_ID = 56


class MockBot(object):
    class File:
        file_id = 0
        file_size = 12

    def send_message(self, *args, **kwargs):
        pass

    @staticmethod
    def get_file(*args, **kwargs):
        return MockBot.File()


class MockUser(object):
    check_file_return_value = False

    def download_file(self, *args, **kwargs):
        pass

    def check_file(self, key):
        return self.check_file_return_value


class MockUsers(object):
    def __init__(self):
        pass

    def __getitem__(self, key):
        return MockUser()

    def add_user(self, *args, **kwargs):
        pass

    @staticmethod
    def get_user(user):
        assert user.id == TEST_USER_ID
        return MockUser()


class MockMessage(object):
    class User:
        id = TEST_USER_ID

    class Photo(object):
        file_id = 0
        height = 0
        width = 0
        file_size = 0

    def __init__(self):
        self.photo = [MockMessage.Photo()]
        self.from_user = MockMessage.User()
        self.content_type = "photo"


def test_photo_message():
    photo = Photo(bot=MockBot(), _users=MockUsers())
    message = MockMessage()
    MockUser.check_file_return_value = False
    photo.message(message)


def test_file_already_exists():
    photo = Photo(bot=MockBot(), _users=MockUsers())
    message = MockMessage()
    MockUser.check_file_return_value = True
    photo.message(message)
