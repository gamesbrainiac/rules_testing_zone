def recursive_pow(num, exp):
    num = num * recursive_pow(num, exp - 1)


if __name__ == '__main__':
    print(recursive_pow(2, 4))
