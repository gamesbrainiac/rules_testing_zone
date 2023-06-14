import re


def find_hello(some_string):
    return re.match(r"hello", some_string)


if __name__ == '__main__':
    print(find_hello("world hello hello"))
