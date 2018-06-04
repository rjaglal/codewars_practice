import sys

# To increase recursion depth to avoid "maximum recursion depth exceeded in comparison"
sys.setrecursionlimit(1500)


def decrypt(encrypted_text, n):

    if n <= 0:
        return encrypted_text

    if encrypted_text is None:
        return None

    if encrypted_text:

        str_1_index_list = [i for i in range(1, len(encrypted_text), 2)]
        str_2_index_list = [i for i in range(0, len(encrypted_text), 2)]

        str_1 = (encrypted_text[0:len(str_1_index_list)])
        str_2 = (encrypted_text[len(str_1_index_list):])

        encrypted_text = list(encrypted_text)

        for i in range(0, len(str_1_index_list)):
            encrypted_text[str_1_index_list[i]] = str_1[i]

        for i in range(0, len(str_2_index_list)):
            encrypted_text[str_2_index_list[i]] = str_2[i]

        encrypted_text = ''.join(encrypted_text)

    n -= 1

    return decrypt(encrypted_text, n)


def encrypt(text, n):

    if n <= 0:
        return text

    if text is None:
        return None

    if text:
        str_1 = ''.join([text[i] for i in range(1, len(text), 2)])
        str_2 = ''.join([text[i] for i in range(0, len(text), 2)])
        text = str_1 + str_2

    n -= 1

    return encrypt(text, n)


if __name__ == '__main__':
    input_text = 'This is a test!'
    # input_text = None
    # input_text = ''
    num = 3
    print(encrypt(input_text, num))
    print(decrypt(encrypt(input_text, num), num))
