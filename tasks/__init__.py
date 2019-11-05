from invoke import task
import tasks.bot_control as bot_control
from logger import log

log.set_level(log.INFO)


@task
def start(_):
    bot_control.start()


@task
def status(_):
    bot_control.status()


@task
def stop(_):
    bot_control.stop()


@task
def start_manager(_):
    bot_control.start_manager()


@task
def status_manager(_):
    bot_control.status_manager()


@task
def stop_manager(_):
    bot_control.stop_manager()


@task
def gen_config(_):
    bot_control.gen_config()
