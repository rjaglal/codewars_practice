import math


def find_next_square(n):

    if (math.sqrt(n)).is_integer():
        return int((math.sqrt(n) + 1)**2)
    else:
        return -1


if __name__ == '__main__':
    number = 121
    print(find_next_square(number))
