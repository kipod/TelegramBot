import os
from bot.server import Server


def main():

    with open('PID', 'w') as file:
        file.write(str(os.getpid()))
    try:
        srv = Server()
        srv.run()
    finally:
        os.remove('PID')


if __name__ == '__main__':
    main()
