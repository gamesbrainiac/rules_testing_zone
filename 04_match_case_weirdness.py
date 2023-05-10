def match_test(seq):

    match seq:
        case []:
            print("Empty list")
        case [x, ]:
            print("List with one item")
        case [x, y]:
            print("List with two items")
        case _:
            print("Other")


if __name__ == '__main__':
    match_test((1, 2))
