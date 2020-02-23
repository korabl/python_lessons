translateDict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')

with open('task4.txt', 'r') as f:
    for line in f:
        wordList = line.split()
        for word in wordList:
            if word.isalpha():
                rusWord = translateDict.get(word)
                lastText = (' '.join(wordList[1:]))
        with open('task4_rus.txt', 'a') as w:
            w.write(rusWord + ' ' + lastText + '\n')

