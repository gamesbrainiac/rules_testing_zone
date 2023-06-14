def times_table():
    table = []
    for i in range(10):
        def multiplier(x):
            return i * x

        table.append(multiplier)

    return table


if __name__ == '__main__':
    print([f(5) for f in times_table()])
