with open('task5.txt', 'w') as f:
    f.write(input('Text: '))

with open('task5.txt', 'r') as f:
    for line in f:
        numList = line.split()
        numSum = 0
        for n in numList:
            n = int(n)
            numSum += n
        print(numSum)
