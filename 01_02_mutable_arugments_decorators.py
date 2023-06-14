from functools import wraps


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        return func(*args, **kwargs)

    return wrapper

@logger
def add_item(item, items=[]):
    items.append(item)
    return items


if __name__ == '__main__':
    print(add_item(1))
    print(add_item(2))
    print(add_item(3))
