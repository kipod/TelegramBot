from invoke import task
from logger import log

@task
def start(_):
    log(log.INFO, "starting...")
    pass


@task
def status(_):
    pass


@task
def stop(_):
    pass
