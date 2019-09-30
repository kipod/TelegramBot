class MyError(Exception):
    def __repr__(self):
        return "bububu"

    def __str__(self):
        return "my exception"


def fun1(a):
    if a == 7:
        raise MyError()
    pass
    return 56


def main():
    try:
        res = fun1(8)
        if res:
            pass
        print("OK")
    finally:
        print("all cool!")


if __name__ == '__main__':
    try:
        main()
    except MyError:
        print("wrong value!")
