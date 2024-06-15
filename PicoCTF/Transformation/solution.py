with open("enc", "r", encoding="utf-8") as file:

    encrypted = file.read()


# encrypted = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])


flag = ""
for character in encrypted:

    ascii_val = ord(character)  # get the ASCII value of the character

    high = ascii_val >> 8  # shift right by 8 bits

    low = ascii_val & 0xFF  # bitwise AND with 0xFF to get the last 8 bits
    flag += chr(high) + chr(low)  # convert the high and low bytes to characters


print(flag)
