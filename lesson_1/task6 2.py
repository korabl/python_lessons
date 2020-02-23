current_result = int(input('Введите текущее кол-во км: '))
wish_result = int(input('Введите желаемое кол-во км: '))

days = 1
while current_result <= wish_result:
    current_result *= 1.1
    days += 1

print(days)