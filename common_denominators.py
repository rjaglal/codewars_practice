from functools import reduce


def convertFracts(lst):

    common_div_list = [item[-1] for item in lst]
    # GCD(greatest common divisor) or HCF(highest common factor)
    # can only be done between two integers at a time
    # LCM  can only be done between two integers at a time
    lcm_val = reduce(lambda a, b: a * b // gcd(a, b), common_div_list)
    output_list = [[(lcm_val // item[-1]) * item[0], lcm_val] for item in lst]

    return output_list


def gcd(x, y):
    # This function implements the Euclidian algorithm to find H.C.F. of two numbers
    while y:
        x, y = y, x % y
    return x


if __name__ == '__main__':
    input_data = [[69, 130], [87, 1310], [3, 4]]
    output_expected = [[18078, 34060], [2262, 34060], [25545, 34060]]
    print(convertFracts(input_data))
