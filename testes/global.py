a = 1
b = 2
c = 3


def primeira():
    a = 4
    print(a, b, c)
    segunda()


def segunda():
    global b
    b = 5
    print(a, b, c)


def main():
    print(a, b, c)
    primeira()
    print(a, b, c)


if __name__ == "__main__":
    main()
