import telebot
import psutil
import subprocess
import signal
from logger import log
from bot.config import CONFIG
import tasks.bot_control as bot_control

log.set_level(log.DEBUG)


class BotManager(object):

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
        subprocess.Popen('invoke start', shell=True)
        # process = subprocess.Popen('invoke start', shell=True,
        #                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.DEVNULL)
        # TODO write output from bot
        # try:
        #     outputs, errors = process.communicate(timeout=5)
        # except subprocess.TimeoutExpired:
        #     process.kill()
        #     outputs, errors = process.communicate()
        # pass

    def status(self, message):
        self.bot.send_message(message.from_user.id, "Running" if bot_control.is_running() else "Stopped")

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
