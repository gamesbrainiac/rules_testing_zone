def always_none():
    return None


def main(param='a'):
    if always_none():
        print("Something")


if __name__ == '__main__':
    main('b')
