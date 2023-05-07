import math


def pow_(x, y):
    return math.pow(x, y)


def main(param='a'):
    if param == 'a':
        print(pow_(2, 3))
    else:
        print(math.pow(2, 3))


if __name__ == '__main__':
    main()
