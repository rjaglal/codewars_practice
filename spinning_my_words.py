def spin_words(sentence):

    list_of_words = sentence.split()

    for i in range(0, len(list_of_words)):
        if len(list_of_words[i]) > 4:
            list_of_words[i] = list_of_words[i][::-1]

    return ' '.join(list_of_words)


if __name__ == '__main__':
    full_string = 'Welcome Hello World Ravi'
    spin_words(full_string)
