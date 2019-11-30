from bot.users import users


class Message(object):
    def __init__(self, bot, _users=users):
        self.bot = bot
        self.name = ''
        self.surname = ''
        self.age = 0
        self.users = _users
