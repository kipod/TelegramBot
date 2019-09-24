import psutil as ps
from invoke import task
from logger import log

log.set_level(log.DEBUG)


@task
def start(_):
    if is_running():
        log(log.INFO, "already started")
        return
    log(log.INFO, "starting...")
    pass


def is_running() -> bool:
    with open('PID', 'r') as file:
        pid = int(file.readline())
        return ps.pid_exists(pid)
    # noinspection PyUnreachableCode
    return False


@task
def status(_):
    log(log.DEBUG, "get status")
    log(log.INFO, 'running' if is_running() else 'stopped')


@task
def stop(_):
    log(log.INFO, "stopping...")
