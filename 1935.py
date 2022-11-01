#1935
def canBeTypedWords(text: str, brokenLetters: str):
    text_list = text.split(sep=" ")
    letter_list = list(brokenLetters)
    finalCount = 0
    for text in text_list:
        count = 0
        for letter in letter_list:
            if letter in text:
                break
            else:
                count += 1
        if count == len(letter_list):
            finalCount += 1
    return finalCount