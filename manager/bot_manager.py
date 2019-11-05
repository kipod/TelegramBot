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
        log(log.INFO, 'starting manager bot')
        me = self.get_me()
        for attr in me:
            log(log.INFO, "%s: %s", attr, me[attr])
        self.bot.polling(none_stop=True, interval=0)

    def get_me(self):
        me = self.bot.get_me()
        attributes = [a for a in dir(me) if not a.startswith('_') and not callable(getattr(me, a))]
        return {a: getattr(me, a) for a in attributes}
