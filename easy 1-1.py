def lengthOfLastWord(s: str) -> int:
    lastWordLength = 0
    currentWordLength = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            currentWordLength += 1
        else:
            lastWordLength = max(lastWordLength, currentWordLength)
            currentWordLength = 0

    return max(lastWordLength, currentWordLength)

s = input("Enter a string: ")
lastWordLength = lengthOfLastWord(s)
print("Length of last word:", lastWordLength)