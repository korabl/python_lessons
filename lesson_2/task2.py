my_list = []
count = int(input('Введите кол-во элементов списка: '))
i = 0
while i < count:
    number = int(input('Введите число: '))
    my_list.append(number)
    i += 1
print(my_list)

n = int(len(my_list)/2)
i = 0
for el in range(n):
    first_el = my_list[i]
    second_el = my_list[i+1]
    my_list.pop(i)
    my_list.insert(i, second_el)
    my_list.pop(i+1)
    my_list.insert(i+1, first_el)
    i += 2
print(my_list)