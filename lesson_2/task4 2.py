text = input('Введите какой-нибудь текст: ')
wordList = text.split()
punctuation = ['.',',',':',';','!','?','(',')']
i = 0
for word in wordList:
    if word[-1] in punctuation:
        wordList[i] = word[:-1]
        word = wordList[i]
    if word[0] in punctuation:
        wordList[i] = word[1:]
    i += 1

i = 1
for word in wordList:
    if len(word) > 10:
        print(f'{i} {word[:10]}')
    else:
        print(f'{i} {word}')
    i += 1