import os

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
        log(log.INFO, 'starting... ')
        self.bot.polling(none_stop=True, interval=0)
