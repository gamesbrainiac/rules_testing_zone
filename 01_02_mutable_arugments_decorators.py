from functools import wraps


def logger(func):
    """
    Logger that logs the function name and arguments
    when it is called
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)

    return wrapper

@logger
def add_item(item, items=[]):
    """
    A function that adds an item to an existing list.
    If a list is not provided, it creates a new item
    with that list added.
    """
    items.append(item)
    return items


if __name__ == '__main__':
    print(add_item(1))
    print(add_item(2))
    print(add_item(3))
