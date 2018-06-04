alphabet_a_to_z = list(map(chr, range(97, 123)))
alphabet_A_to_Z = list(map(chr, range(65, 91)))
num_0_9 = list(map(str, range(10)))
acceptable_chars = ['.', ',', ':', ';', '-',
                    '?', '!', ' ', '\'', '(',
                    ')', '$', '%', '&', '"']
region_list = alphabet_A_to_Z + alphabet_a_to_z + num_0_9 + acceptable_chars

# data = [(k, i) for k, i in enumerate(region_list)]
# print(data)


# Reverse the Steps to decrypt the message
def decrypt(encrypted_text):
    if encrypted_text in ("", None):
        return encrypted_text

    if not set(encrypted_text).issubset(set(region_list)):
        raise Exception

    new_decrypted_text = list(encrypted_text)

    # Step 3; Reverts the Mirror from the region list
    new_decrypted_text[0] = region_list[(len(region_list) - 1) - region_list.index(new_decrypted_text[0])]

    # Step 2
    for i in range(1, len(new_decrypted_text)):
        char_current_region_index = region_list.index(new_decrypted_text[i])
        char_before_region_index = region_list.index(new_decrypted_text[i - 1])
        diff = char_before_region_index - char_current_region_index
        new_decrypted_text[i] = region_list[diff]

    # Step 1; Sets every second char to a switch of case;
    # upper to lower; lower to upper
    for i in range(1, len(new_decrypted_text), 2):
        new_decrypted_text[i] = new_decrypted_text[i].swapcase()

    return ''.join(new_decrypted_text)


def encrypt(text):

    if text in ("", None):
        return text

    if not set(text).issubset(set(region_list)):
        raise Exception

    new_text = list(text)

    # Step 1; Sets every second char to a switch of case;
    # upper to lower; lower to upper
    for i in range(1, len(new_text), 2):
        new_text[i] = new_text[i].swapcase()

    # print(new_text)

    encrypted_list = []
    for i in range(0, len(new_text)):
        char_current_region_index = region_list.index(new_text[i])

        # Step 3; I did this before because I am writing the output to a new list
        if i == 0:
            encrypted_list.append(region_list[(len(region_list) - 1) - char_current_region_index])
        # Does not affect the first element in the text
        # Step 2
        else:
            char_before_region_index = region_list.index(new_text[i - 1])
            diff = char_before_region_index - char_current_region_index
            # Below comment is for troubleshooting
            # print(new_text[i], char_before_region_index, char_current_region_index, diff, region_list[diff])
            encrypted_list.append(region_list[diff])

    # Return encrypted string
    return ''.join(encrypted_list)


if __name__ == '__main__':
    # input_str = 'This is a test!'
    input_str_en = 'Business'
    input_str_de = '&61kujla'
    print(encrypt(input_str_en))
    print(decrypt(input_str_de))
