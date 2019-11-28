from bot.users import users


class Message(object):
    def __init__(self, bot):
        self.bot = bot
        self.name = ''
        self.surname = ''
        self.age = 0

    @staticmethod
    def check_user(user):
        u = users[str(user.id)]
        if not u:
            users.add_user(uid=user.id, name=user.first_name, surname=user.last_name, username=user.username)

    @staticmethod
    def check_file(file, uid, content_type):
        user = users[str(uid)]
        user_file = user.get_file_by_id(file.file_id)
        if not user_file:
            user.add_file(file_id=file.file_id, content_type=content_type, file_path=file.file_path)
            return False
        else:
            return True
