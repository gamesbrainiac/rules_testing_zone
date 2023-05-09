def recursive_pow(num, exp):
    if exp > 1:
        num = num * recursive_pow(num, exp - 1)
    return num


if __name__ == '__main__':
    print(recursive_pow(2, 4))
