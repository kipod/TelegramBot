import os
for env in os.environ:
    print(env, "=", os.environ[env])

from bot import Server


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
