from invoke import task
import tasks.bot_control as bot_control
from logger import log

log.set_level(log.DEBUG)


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
def gen_config(_):
    bot_control.gen_config()