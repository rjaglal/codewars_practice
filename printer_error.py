def print_error(s):
    alphabet_n_to_z = list(map(chr, range(110, 123)))

    # Count increment with a list comprehension
    error_count = [1 for ele in s if ele in alphabet_n_to_z].count(1)

    return "{}/{}".format(error_count, len(s))


if __name__ == '__main__':
    input_str = 'aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz'
    print(print_error(input_str))
