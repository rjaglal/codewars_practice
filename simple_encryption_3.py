alphabet_a_to_z = list(map(chr, range(97, 123)))
alphabet_A_to_Z = list(map(chr, range(65, 91)))
num_0_9 = list(map(str, range(10)))
acceptable_chars = [' ', '.']
region_list = alphabet_A_to_Z + alphabet_a_to_z + num_0_9 + acceptable_chars

# Below is for troubleshooting. It make all element in tuples with there respective index
# data = [(k, i) for k, i in enumerate(region_list)]
# print(data)


def decrypt(encrypted_text):

    if encrypted_text in ("", None):
        return encrypted_text

    if not set(encrypted_text).issubset(set(region_list)):
        raise Exception

    encrypted_text = chars_to_bits(encrypted_text)
    # print(encrypted_text)

    # To decrypt the message we must reverse the steps
    # Decrement a "for" loop
    for i in range(len(encrypted_text) - 1, -1, -1):
        # print(encrypted_text[i])
        char_bits = encrypted_text[i]

    # 6. Change the first against the third bit of the char. (1 <==> 3)
        char_bits[0], char_bits[2] = char_bits[2], char_bits[0]
        # print("Reverse Step 6 {}".format(char_bits))

    # 5. Reverse the whole line of bits of the char.
        char_bits.reverse()
        # print("Reverse Step 5 {}".format(char_bits))

    # 4. Change every odd bit against the following bit of the char. (1 <==> 2, 3 <==> 4, 5 <==> 6)
        char_bits[0], char_bits[1] = char_bits[1], char_bits[0]
        char_bits[2], char_bits[3] = char_bits[3], char_bits[2]
        char_bits[4], char_bits[5] = char_bits[5], char_bits[4]
        # print("Reverse Step 4 {}".format(char_bits))

    # 3. Change the first 3 bit against the last 3 bit of the char. (1,2,3 <==> 4,5,6)
        char_bits[:3], char_bits[3:] = char_bits[3:], char_bits[:3]
        # print("Reverse Step 3 {}".format(char_bits))

    # 2. Inverse the second and the forth bit of the char. (2,4 => 0->1 or 1->0)
        char_bits[1] = "0" if "1" in char_bits[1] else "1"
        char_bits[3] = "0" if "1" in char_bits[3] else "1"
        # print("Reverse Step 2 {}".format(char_bits))

    # 1. Change the fifth bit of the char and the first bit of the next char.
    # (C1.5 <==> C2.1, only if there is a next char!)

        if i < len(encrypted_text) - 1:
            previous_char_bits = encrypted_text[i + 1]
            char_bits[4], previous_char_bits[0] = previous_char_bits[0], char_bits[4]

        # print("Reverse Step 1 {}".format(char_bits))

    return bit_to_chars(encrypted_text)


def chars_to_bits(string_data):

    list_of_lists_of_bits = []

    for i in range(0, len(string_data)):
        char_region_index = region_list.index(string_data[i])
        # Converts a integer to binary
        char_bits = "{0:b}".format(char_region_index)
        # Ensures that there are 6 integers. Fills in the needs integers with zeros
        char_bits = '{:06}'.format(int(char_bits))
        char_bits = list(char_bits)
        list_of_lists_of_bits.append(char_bits)

    return list_of_lists_of_bits


def bit_to_chars(list_of_bit_chars):

    output_string_chars = ''

    for item in list_of_bit_chars:
        bit_string = ''.join(item)
        # Takes a string of numbers and converts it from base 2
        int_val = int(bit_string, 2)
        region_char = region_list[int_val]
        output_string_chars = output_string_chars + region_char

    return output_string_chars


def encrypt(text):

    if text in ("", None):
        return text

    if not set(text).issubset(set(region_list)):
        raise Exception

    text = chars_to_bits(text)

    for i in range(0, len(text)):

        char_bits = text[i]

        # 1. Change the fifth bit of the char and the first bit of the next char.
        # (C1.5 <==> C2.1, only if there is a next char!)
        if i < len(text) - 1:
            next_char_bits = text[i + 1]
            hold_var = char_bits[4]
            char_bits[4] = next_char_bits[0]
            next_char_bits[0] = hold_var
        # print("Step 1 {}".format(char_bits))

        # 2. Inverse the second and the forth bit of the char. (2,4 => 0->1 or 1->0)
        char_bits[1] = '1' if '0' in char_bits[1] else '0'
        char_bits[3] = '1' if '0' in char_bits[3] else '0'
        # print("Step 2 {}".format(char_bits))

        # 3. Change the first 3 bit against the last 3 bit of the char. (1,2,3 <==> 4,5,6)
        char_bits[:3], char_bits[3:] = char_bits[3:], char_bits[:3]
        # print("Step 3 {}".format(char_bits))

        # 4. Change every odd bit against the following bit of the char. (1 <==> 2, 3 <==> 4, 5 <==> 6)
        char_bits[0], char_bits[1] = char_bits[1], char_bits[0]
        char_bits[2], char_bits[3] = char_bits[3], char_bits[2]
        char_bits[4], char_bits[5] = char_bits[5], char_bits[4]
        # print("Step 4 {}".format(char_bits))

        # 5. Reverse the whole line of bits of the char.
        char_bits.reverse()
        # print("Step 5 {}".format(char_bits))

        # 6. Change the first against the third bit of the char. (1 <==> 3)
        char_bits[0], char_bits[2] = char_bits[2], char_bits[0]
        # print("Step 6 {}".format(char_bits))

    return bit_to_chars(text)


if __name__ == '__main__':
    # input_text = 'Do the kata Kobayashi Maru Test. Endless fun and excitement when finding a solution.'
    # expected_output = 'rfR9qRVMT8TUfeyXGXdrLUcT.dUmVd5xUNo1oRdZQ1dtUXs1QVmRL8RMVt9RHqRtU1Ps1LtPQXVdbpZ9Lfp1'
    # print(input_text)
    # print(encrypt(input_text))
    # if encrypt(input_text) in expected_output:
    #     print(True)
    # else:
    #     print(False)
    input_text = 'jvLdRPdQXV8Rd5x'
    print(decrypt(input_text))
