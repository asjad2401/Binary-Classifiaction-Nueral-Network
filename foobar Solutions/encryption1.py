def solution(x):
    output = ""
    for letter in x:
        if 'a' <= letter <= 'z':
            replacedLetter = chr(ord('a') + ord('z')- ord(letter))
            output += replacedLetter
        else:
            output += letter
    return output
    
inputSentence = input()
print(solution(inputSentence))