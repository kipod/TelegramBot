from invoke import task
from logger import log

log.set_level(log.DEBUG)


@task
def start(_):
    log(log.INFO, "starting...")
    pass


@task
def status(_):
    log(log.DEBUG, "get status")


@task
def stop(_):
    log(log.INFO, "stopping...")
