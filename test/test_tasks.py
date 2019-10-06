import os
from tasks.bot_control import gen_config
from bot.config import Configuration, CONFIG_FILE_NAME
from logger import log

COPY_CONFIG_FILE_NAME = CONFIG_FILE_NAME + '.bak'


def setup():
    log(log.INFO, 'setup')
    if os.path.exists(CONFIG_FILE_NAME):
        os.rename(CONFIG_FILE_NAME, COPY_CONFIG_FILE_NAME)


def teardown():
    log(log.INFO, 'teardown')
    if os.path.exists(CONFIG_FILE_NAME):
        os.remove(CONFIG_FILE_NAME)
    if os.path.exists(COPY_CONFIG_FILE_NAME):
        os.rename(COPY_CONFIG_FILE_NAME, CONFIG_FILE_NAME)


def test_gen_config():
    os.environ['BOT_TOKEN'] = 'TEST_TOKEN1'
    os.environ['BOT_MGR_TOKEN'] = 'TEST_TOKEN2'
    assert gen_config()
    cfg = Configuration()
    assert cfg.bot_token == 'TEST_TOKEN1'
    assert cfg.bot_manager_token == 'TEST_TOKEN2'
