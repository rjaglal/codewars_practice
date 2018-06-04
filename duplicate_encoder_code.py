def duplicate_encode(word):

    encoded_list = []
    word = word.upper()

    for ele in word:
        if word.count(ele) > 1:
            encoded_list.append(')')
        else:
            encoded_list.append('(')

    return ''.join(encoded_list)


if __name__ == '__main__':
    str_word = "Success"
    print(duplicate_encode(str_word))
