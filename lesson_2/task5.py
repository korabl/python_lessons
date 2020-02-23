number = int(input('Введите число: '))
my_list = [7, 5, 3, 3, 2]

i = 0
for el in my_list:
    if my_list[i] <= number:
        my_list.insert(i, number)
        break
    else:
        my_list.append(number)
        break
    i += 1

print(my_list)