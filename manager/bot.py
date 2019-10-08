import os
import telebot
import psutil
import subprocess
import signal
from logger import log

log.set_level(log.DEBUG)

MNG_BOT_TOKEN = os.environ['MNG_BOT_TOKEN']


class Bot(object):

    def __init__(self):
        MESSAGE_MAP = {
            "/start": self.start,
            "/status": self.status,
            "/stop": self.stop
        }
        self.bot = telebot.TeleBot(MNG_BOT_TOKEN)

        @self.bot.message_handler(content_types=['text'])
        def on_message(message):
            if message.text in MESSAGE_MAP:
                MESSAGE_MAP[message.text](message)
            else:
                pass

    def start(self, message):
        if Bot.is_running():
            self.bot.send_message(message.from_user.id, "Bot already started")
            log(log.INFO, 'get_text_messages %s', message.text)
            return
        self.bot.send_message(message.from_user.id, "Starting dJg.Test.Bot...")
        subprocess.Popen('start python bot.py', shell=True)

    def status(self, message):
        if Bot.is_running():
            self.bot.send_message(message.from_user.id, "Running")
            return
        self.bot.send_message(message.from_user.id, "Stopped")

    def run(self):
        log(log.INFO, 'starting... ')
        self.bot.polling(none_stop=True, interval=0)

    def stop(self, message):
        if Bot.is_running():
            self.bot.send_message(message.from_user.id, "Process was started")
            pid = Bot.get_pid()
            p = psutil.Process(pid)
            self.bot.send_message(message.from_user.id, "Stopping...")
            try:
                p.send_signal(signal.CTRL_C_EVENT)
            except SystemError:
                pass
            _, alive = psutil.wait_procs([p], timeout=2)
            for p in alive:
                self.bot.send_message(message.from_user.id, "Terminating...")
                p.terminate()
        else:
            self.bot.send_message(message.from_user.id, "The process was not started")

    @staticmethod
    def get_pid():
        with open('PID', 'r') as file:
            return int(file.readline())

    @staticmethod
    def is_running() -> bool:
        try:
            return psutil.pid_exists(Bot.get_pid())
        except FileNotFoundError:
            return False


