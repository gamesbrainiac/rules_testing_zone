def add_item(item, items=[]):
    items.append(item)
    return items


if __name__ == '__main__':
    v = add_item(1)
    print(add_item(2))
    print(add_item(3))
    print(add_item(4))
    print(v)
