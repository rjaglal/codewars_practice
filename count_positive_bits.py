def count_bits(n):

    string_of_bits = "{0:b}".format(n)
    print(string_of_bits)
    return string_of_bits.count('1')


if __name__ == '__main__':
    number = 37
    print(count_bits(number))
