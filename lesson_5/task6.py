from itertools import groupby

lessons = {}

with open('task6.txt', 'r') as f:
    for line in f:
        sumHour = 0
        numList = [''.join(i) for is_digit, i in groupby(line, str.isdigit) if is_digit]
        for n in numList:
            n = int(n)
            sumHour += n
        wordList = line.split()
        lessons.setdefault(wordList[0], sumHour)

print(lessons)

