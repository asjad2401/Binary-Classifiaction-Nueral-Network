def solution(x):
    decoded = ""
    for char in x:
        if char.isalpha():
            shifted = ord(char) - 7 if char.islower() else ord(char) - \
                7 if char.isupper() else ord(char)
            if shifted < ord('a') and char.islower():
                shifted += 26
            elif shifted < ord('A') and char.isupper():
                shifted += 26
            decoded += chr(shifted)
        else:
            decoded += char
    return decoded


input_string = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
output = solution(input_string)
print(output)



