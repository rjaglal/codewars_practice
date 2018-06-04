def persistence(n, count=0):

    mul_num = -1
    if n < 10:
        return count
    else:
        count += 1

    n_str = str(n)
    for num in n_str:
        if mul_num < 0:
            mul_num = int(num)
            continue
        mul_num = int(num) * mul_num

    print(mul_num)

    if mul_num > 9:
        return persistence(mul_num, count)
    else:
        return count


if __name__ == '__main__':
    ele = 4
    print("Count = {}".format(persistence(ele)))
