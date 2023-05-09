def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


if __name__ == '__main__':
    add_item(2)
    add_item(3)
    print(add_item(4))
