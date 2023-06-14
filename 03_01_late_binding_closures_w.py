def times_table():
    """
    Returns a list of functions that will give you
    the times table.

    >>> [f(5) for f in times_table()]
    >>> [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    """
    table = []
    for i in range(10):
        def multiplier(x):  # This is a closure, because it has access to its outer lexical scope
            return i * x  # lookup for the variable i happens when the variable is used, not when it defined.

        table.append(multiplier)

    return table


if __name__ == '__main__':
    print([f(5) for f in times_table()])
