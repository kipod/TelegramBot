import os
from builtins import getattr

import telebot

from .parser import Text, Photo
from logger import log

BOT_TOKEN = os.environ['BOT_TOKEN']


class Server:
    def __init__(self):
        self.bot = telebot.TeleBot(BOT_TOKEN)
        self.handler = {
            'text': Text(self.bot),
            'photo': Photo(self.bot)
        }

        @self.bot.message_handler(content_types=['text', 'photo'])
        def _get_text_messages(message):
            log(log.INFO, "received [%s]", message.content_type)
            self.handler[message.content_type].message(message)

    def run(self):
        log(log.INFO, 'starting bot server... ')
        me = self.get_me()
        for attr in me:
            log(log.INFO, "%s: %s", attr, me[attr])
        self.bot.polling(none_stop=True, interval=0)

    def get_me(self):
        me = self.bot.get_me()
        attributes = [a for a in dir(me) if not a.startswith('_') and not callable(getattr(me, a))]
        return {a: getattr(me, a) for a in attributes}
