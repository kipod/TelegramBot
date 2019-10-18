from subprocess import Popen, PIPE

import telebot

from bot.config import CONFIG
from logger import log

log.set_level(log.DEBUG)


class BotManager(object):

    def __init__(self):
        self.bot = telebot.TeleBot(CONFIG.bot_manager_token)

        @self.bot.message_handler(content_types=['text'])
        def on_message(message):
            args = ['invoke', message.text]
            process = Popen(args, stdout=PIPE, stderr=PIPE)
            stdout, stderr = process.communicate()
            for line in [l.strip() for l in (stderr + stdout).decode().split('\n') if l.strip()]:
                self.bot.send_message(message.from_user.id, line)

    def run(self):
        log(log.INFO, 'starting... ')
        self.bot.polling(none_stop=True, interval=0)
