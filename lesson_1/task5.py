revenue = int(input('Введите выручку (т.р.): '))
cogs = int(input('Введите издержки (т.р.): '))
profit = revenue - cogs
if profit < 0:
    print('Убыток')
elif profit == 0:
    print('Вы работаете в ноль')
else:
    print('Прибыль')
    rent = revenue/cogs
    print(f'Рентабельность: {rent}')
    employers = int(input('Введите кол-во сотрудников: '))
    print(f'Прибыль в расчете на 1-го сотрудника: {profit/employers} т.р.')
