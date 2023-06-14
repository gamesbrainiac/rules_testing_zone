def add_item(item, items=[]):
    """
    A function that adds an item to an existing list.
    If a list is not provided, it creates a new item
    with that list added.
    """
    items.append(item)
    return items


if __name__ == '__main__':
    v = add_item(1)
    print(add_item(2))
    print(add_item(3))
    print(add_item(4))
    print(v)
