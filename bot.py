import os
from bot import Server


# main function
def main():

    with open('PID', 'w') as file:
        file.write(str(os.getpid()))
    try:
        srv = Server()
        srv.run()
    finally:
        os.remove('PID')


# name main
if __name__ == '__main__':
    main()
