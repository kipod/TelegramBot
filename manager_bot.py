import os
from manager.bot_manager import BotManager


def main():

    with open('MNG_PID', 'w') as file:
        file.write(str(os.getpid()))
    try:
        mng = BotManager()
        mng.run()
    finally:
        os.remove('MNG_PID')


if __name__ == '__main__':
    main()
