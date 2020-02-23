m = int(input('Введите ставку р/час: '))
h = int(input('Введите кол-во часов: '))
b = int(input('Введите премию: '))

def salary(money, houres, bonus):
    return (money * houres) + bonus

print(salary(m, h, b))