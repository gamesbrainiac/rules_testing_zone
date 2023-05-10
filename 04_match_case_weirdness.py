def match_test(seq):

    x, y = 10, 10

    match seq:
        case []:
            print("Empty list")
        case [x, ]:
            print("List with one item")
        case [x, y]:
            print("List with two items")
        case _:
            print("Other")

    print(x, y)


if __name__ == '__main__':
    match_test((1, 2))
