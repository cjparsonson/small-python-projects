def string_to_binary():
    user_string = input('Enter a string: ')
    bin_conv = [format(ord(character), 'b') for character in user_string]
    return ' '.join(bin_conv)


def string_to_hex():
    user_string = input('Enter a string: ')
    hex_conv = [format(ord(character), 'x') for character in user_string]
    return ' '.join(hex_conv)


def binary_to_ascii():
    user_input = input('Enter a binary character or string: ')
    bytes_list = user_input.split()
    ascii_conversion = [chr(int(character, 2)) for character in bytes_list]
    return ''.join(ascii_conversion)


# Testing - uncomment as needed

# print(string_to_binary())
# print(string_to_hex())
# print(binary_to_ascii())
