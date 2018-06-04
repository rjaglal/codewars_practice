def productFib(prod):

    n = 0
    mul_val = 0
    # Since n = 0 the Fib number is 0
    val_n = 0
    while mul_val < prod:
        val_n_1 = fib(n + 1)
        mul_val = val_n * val_n_1
        if mul_val == prod:
            return [val_n, val_n_1, True]
        elif mul_val > prod:
            return [val_n, val_n_1, False]
        n += 1
        val_n = val_n_1


# Recursion is slower that loops
def fib_func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_func(n-1) + fib_func(n-2)


# Faster than recursion
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a+b
    return a


if __name__ == '__main__':
    input_data = 4895
    print(productFib(input_data))
    # print(fib_func(21))
