numbers = []

while True:
    number = input('Выход - Q, \nВведите числа: ')
    numberList = number.split()
    outList = []
    for n in numberList:
        if n.upper() == 'Q':
            outList.append(n)
            numberList.remove(n)
        else:
            numbers.append(int(n))

    print(sum(numbers))
    if outList:
        break






