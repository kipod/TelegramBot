import invoke
from logger import log
import task

log.set_level(log.DEBUG)


@invoke.task
def start(_):
    task.start()


@invoke.task
def status(_):
    task.status()


@invoke.task
def stop(_):
    task.stop()
