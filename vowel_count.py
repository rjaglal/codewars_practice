def get_count(in_str):

    vowels = ['a', 'e', 'i', 'o', 'u']

    only_vowels = [ele for ele in in_str if ele in vowels]

    return len(only_vowels)


if __name__ == '__main__':
    input_string = 'abracadabra'
    print(get_count(input_string))
