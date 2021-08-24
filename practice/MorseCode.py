morse_dict = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"}
morse_code = ".... . .-.. .-.. ---  .-- --- .-. .-.. -.."


def decode(string):                               # 把摩尔斯码转成英文
    if string == "":
        return ""
    decoded_string = ""
    word_list = string.split("  ")                # 按照两个空格"  "分开(单词)
    x = 0
    for word in word_list:
        letters = word.split(" ")                 # 吧每个单词按一个空格" "分开(字母)
        for letter in letters:
            decoded_string += morse_dict[letter]  # 查表并把解码内容加到decode_string中
        x = x + 1
        if x != len(word_list):
            decoded_string += " "
    return decoded_string  # 返回decode_string

code = input()
print(code)

print(decode(code))
