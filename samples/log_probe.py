from logger import log

if __name__ == '__main__':
    a = 'bubu'
    log(log.INFO, "Started %d, %s", 1, a)
    log(log.WARNING, "Started %d, %s", 1, a)
    log(log.ERROR, "Started %d, %s", 1, a)
