def times_table():
    table = []
    for i in range(10):
        def multiplier(x, i=i):
            return i * x

        table.append(multiplier)

    return table


if __name__ == '__main__':
    print([f(3) for f in times_table()])
