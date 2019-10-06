import psutil
import subprocess
import signal
from logger import log


def start():
    if is_running():
        log(log.INFO, "already started")
        return
    log(log.INFO, "starting...")
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
    log(log.DEBUG, "get status")
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
        print("The process was not started")
