myText = input('Введите текст: ')

def int_func(text):
    result = []
    wordList = text.split()
    for word in wordList:
        bigWord = word.capitalize()
        result.append(bigWord)
    myString = ' '.join(result)
    print(myString)

int_func(myText)
