def doSomething():  # NOSONAR
    pass


def doSomethingElse():  # NOSONAR
    pass


def print_hi(name):
    a = False
    if a:  # Noncompliant
        doSomething()  # never executed

    n = None

    if not n:  # Noncompliant; n is None, which is always equivalent to "False" in a condition, "doSomethingElse()" is never evaluated
        doSomething()
    else:
        doSomethingElse()  # never executed

    print(f"Helllo {name}")


if __name__ == '__main__':
    print_hi('PyCharm')
