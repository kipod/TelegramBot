import os
import psutil
import subprocess
import signal
import json
from logger import log
from bot.config import CONFIG_FILE_NAME


def start():
    if is_running():
        log(log.INFO, "already started")
        return
    # log(log.INFO, "starting...")
    subprocess.Popen('start python bot.py', shell=True)


def get_pid():
    with open('PID', 'r') as file:
        return int(file.readline())


def is_running() -> bool:
    try:
        return psutil.pid_exists(get_pid())
    except FileNotFoundError:
        return False


def status():
    log(log.INFO, 'running' if is_running() else 'stopped')


def stop():
    if is_running():
        log(log.INFO, "Process was starting...")
        pid = get_pid()
        p = psutil.Process(pid)
        log(log.INFO, "stopping...")
        try:
            p.send_signal(signal.CTRL_C_EVENT)
        except SystemError:
            pass
        _, alive = psutil.wait_procs([p], timeout=2)
        for p in alive:
            log(log.INFO, "terminate...")
            p.terminate()
    else:
        log(log.INFO, "The process was not started" )


def start_manager():
    if mng_is_running():
        log(log.INFO, "already started")
        return
    log(log.INFO, "starting...")
    subprocess.Popen('start python manager_bot.py', shell=True)


def get_mng_pid():
    with open('MNG_PID', 'r') as file:
        return int(file.readline())


def mng_is_running() -> bool:
    try:
        return psutil.pid_exists(get_mng_pid())
    except FileNotFoundError:
        return False


def status_manager():
    log(log.DEBUG, "get status")
    log(log.INFO, 'running' if mng_is_running() else 'stopped')


def stop_manager():
    if mng_is_running():
        log(log.INFO, "Process was starting...")
        mng_pid = get_mng_pid()
        pm = psutil.Process(mng_pid)
        log(log.INFO, "stopping...")
        try:
            pm.send_signal(signal.CTRL_C_EVENT)
        except SystemError:
            pass
        _, alive = psutil.wait_procs([pm], timeout=2)
        for pm in alive:
            log(log.INFO, "terminate...")
            pm.terminate()
    else:
        print("The process was not started")


def gen_config():
    if os.path.exists(CONFIG_FILE_NAME):
        log(log.WARNING, 'The file "%s" already exists', CONFIG_FILE_NAME)
        return False
    BOT_TOKEN = None
    if 'BOT_TOKEN' in os.environ:
        BOT_TOKEN = os.environ['BOT_TOKEN']
    BOT_MGR_TOKEN = None
    if 'BOT_MGR_TOKEN' in os.environ:
        BOT_MGR_TOKEN = os.environ['BOT_MGR_TOKEN']
    conf = {
        'bot_token': BOT_TOKEN,
        'bot_manager_token': BOT_MGR_TOKEN
    }
    with open(CONFIG_FILE_NAME, 'w') as file:
        json.dump(conf, file, indent=2)
    return os.path.exists(CONFIG_FILE_NAME)
