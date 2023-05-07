from util import mylist


def main():
    some_val = mylist[2]
    mylist[3] = 10
    mylist[3] = 12

    return mylist, some_val


if __name__ == '__main__':
    print(main())
