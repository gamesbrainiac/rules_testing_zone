import re


def main():
    match = re.search(r"Jack|Peter|", "John")
    return match


if __name__ == '__main__':
    print(bool(main()))
