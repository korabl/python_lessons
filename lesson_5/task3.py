from itertools import groupby

with open('task3.txt', 'r') as f:
    avSalary = 0
    i = 0
    for line in f:
        l = [''.join(i) for is_digit, i in groupby(line, str.isdigit) if is_digit]
        salary = int(''.join(l))
        avSalary += salary
        i += 1

        personInfo = None
        wordList = line.split()
        for word in wordList:
            if word.istitle():
                personInfo = word

        if salary < 20000:
            print(f'Оклад < 20 т.р. - {salary} руб., {personInfo}')

    print(f'Средний оклад всех сотрудников - {int(avSalary/i)} руб.')

    