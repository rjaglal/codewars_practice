region_1_lower = 'qwertyuiop'
region_2_lower = 'asdfghjkl'
region_3_lower = 'zxcvbnm,.'
region_1_upper = region_1_lower.upper()
region_2_upper = region_2_lower.upper()
region_3_upper = region_3_lower.upper()

region_1_lower = list(region_1_lower)
region_2_lower = list(region_2_lower)
region_3_lower = list(region_3_lower)
region_1_upper = list(region_1_upper)
region_2_upper = list(region_2_upper)
region_3_upper = list(region_3_upper)
region_3_upper[-2], region_3_upper[-1] = '<', '>'

list_of_regions = [region_1_lower, region_2_lower, region_3_lower,
                   region_1_upper, region_2_upper, region_3_upper]


def key_num_to_list_num(key_data):
    # Ensures that the number contains 3 digits. Zeros fill in the empty space
    key_data = '{:03}'.format(key_data)
    return [int(char) for char in str(key_data)]


def find_encrypted_char_in_region(char_data, region_data, key_data):

    # The below is to ensure region 0, 1, 2 is returned so the
    # appropriate key digit is chosen
    combinations = [[0, 3], [1, 4], [2, 5]]

    index_of_region_in_region_list = list_of_regions.index(region_data)
    steps = [key_data[combo[0]] for combo in combinations if index_of_region_in_region_list in combo][0]
    # Since it is encrypting we are just reversing encryption. Therefore the positive sign below
    index_of_encrypted_char = (region_data.index(char_data) + steps) % len(region_data)
    encrypted_char_data = region_data[index_of_encrypted_char]

    return encrypted_char_data


def find_decrypted_char_in_region(char_data, region_data, key_data):

    # The below is to ensure region 0, 1, 2 is returned so the
    # appropriate key digit is chosen
    combinations = [[0, 3], [1, 4], [2, 5]]

    index_of_region_in_region_list = list_of_regions.index(region_data)
    steps = [key_data[combo[0]] for combo in combinations if index_of_region_in_region_list in combo][0]
    # Since it is decrypting we are just reversing encryption. Therefore the negative sign below
    index_of_encrypted_char = (region_data.index(char_data) - steps) % len(region_data)
    decrypted_char_data = region_data[index_of_encrypted_char]

    return decrypted_char_data


def encrypt(text, encryptKey):
    encryptKey = key_num_to_list_num(encryptKey)
    output_chars = []

    for char in text:
        encrypted_char = [find_encrypted_char_in_region(char, region, encryptKey)
                          for region in list_of_regions if char in region]
        # Ensures that if the char is not found in regions that the encrypted_char is set to char
        # Prevents list index out of range exception
        encrypted_char = char if not encrypted_char else encrypted_char[0]
        output_chars.append(encrypted_char)

    return ''.join(output_chars)


def decrypt(text, encryptKey):
    encryptKey = key_num_to_list_num(encryptKey)
    output_chars = []

    for char in text:
        encrypted_char = [find_decrypted_char_in_region(char, region, encryptKey)
                          for region in list_of_regions if char in region]
        # Ensures that if the char is not found in regions that the encrypted_char is set to char
        # Prevents list index out of range exception
        encrypted_char = char if not encrypted_char else encrypted_char[0]
        output_chars.append(encrypted_char)

    return ''.join(output_chars)


if __name__ == '__main__':
    # input_data = 'Wave'
    # input_key = 0
    # print(encrypt(input_data, input_key))

    input_data = 'Iaqh qh g iyhi,'
    input_key = 348
    print(decrypt(input_data, input_key))
