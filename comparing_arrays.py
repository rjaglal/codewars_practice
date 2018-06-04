import math


def comp_func(array1, array2):

    print(array1)
    print(array2)

    if array2 is None or array1 is None:
        return False

    if not array2 and not array1:
        return True

    if len(set(array1)) != len(set(array2)):
        return False

    if (math.sqrt(array2[0])).is_integer():
        if math.sqrt(array2[0]) in array1:
            array1.remove(int(math.sqrt(array2[0])))
            array2.remove(array2[0])
            if not array2 or not array1:
                return True
            else:
                return comp_func(array1, array2)
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    arr1 = [49, 28]
    arr2 = [2401, 785]

    print(comp_func(arr1, arr2))
