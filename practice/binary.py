dec = input("Please put a num here:")
dec = int(dec)
def dec2bin(num):
    binary_num = []
    while (num / 2 != 0):
        num, remainder = divmod(num, 2)
        binary_num.append(remainder)
    binary_num.reverse()
    binary_string = ""
    for digit in binary_num:
        binary_string = binary_string + str(digit)
    return binary_string
print(dec2bin(dec))


