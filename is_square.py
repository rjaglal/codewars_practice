import math


def is_square(n):
    if n < 0:
        return False
    else:
        return (math.sqrt(n)).is_integer()


if __name__ == '__main__':
    num = -1
    print(is_square(num))
