
USE_TEST = True


def test(func):
    if USE_TEST:
        def my_func():
            print('begin')
            func()
            print('end')
        return my_func
    return func

@test
def to_do():
    print("done")


if __name__ == '__main__':
    to_do()
