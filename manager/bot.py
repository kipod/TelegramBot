import telebot
import psutil
import subprocess
import signal
from logger import log
from bot.config import CONFIG
import tasks.bot_control as bot_control

log.set_level(log.DEBUG)


class Bot(object):

    def __init__(self):
        message_map = {
            "/start": self.start,
            "/status": self.status,
            "/stop": self.stop
        }
        self.bot = telebot.TeleBot(CONFIG.bot_manager_token)

        @self.bot.message_handler(content_types=['text'])
        def on_message(message):
            if message.text in message_map:
                message_map[message.text](message)
            else:
                self.bot.send_message(message.from_user.id, "Unknown command")
                pass

    def start(self, message):
        if bot_control.is_running():
            self.bot.send_message(message.from_user.id, "Bot already started")
            log(log.INFO, 'get_text_messages %s', message.text)
            return
        self.bot.send_message(message.from_user.id, "Starting dJg.Test.Bot...")
        subprocess.Popen('start python bot.py', shell=True)  # TODO inv start
        # TODO write output from bot

    def status(self, message):
        if bot_control.is_running():
            self.bot.send_message(message.from_user.id, "Running")
            return
        self.bot.send_message(message.from_user.id, "Stopped")

    def run(self):
        log(log.INFO, 'starting... ')
        self.bot.polling(none_stop=True, interval=0)

    def stop(self, message):
        # TODO by invoke
        if bot_control.is_running():
            self.bot.send_message(message.from_user.id, "Process was started")
            pid = bot_control.get_pid()
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


if __name__ == '__main__':
    bot = Bot()
    bot.run()

    # @staticmethod
    # def get_pid():
    #     # TODO
    #     with open('PID', 'r') as file:
    #         return int(file.readline())
    #
    # @staticmethod
    # def is_running() -> bool:
    #     # TODO
    #     try:
    #         return psutil.pid_exists(Bot.get_pid())
    #     except FileNotFoundError:
    #         return False
