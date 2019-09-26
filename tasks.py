import psutil
import subprocess
from invoke import task
from logger import log

log.set_level(log.DEBUG)


@task
def start(_):
    if is_running():
        log(log.INFO, "already started")
        return
    log(log.INFO, "starting...")
    subprocess.Popen('start python bot.py', shell=True)
    pass


def is_running() -> bool:
    try:
        with open('PID', 'r') as file:
            pid = int(file.readline())
            return psutil.pid_exists(pid)
    except FileNotFoundError:
        return False


@task
def status(_):
    log(log.DEBUG, "get status")
    log(log.INFO, 'running' if is_running() else 'stopped')


@task
def stop(_):
    log(log.INFO, "stopping...")
