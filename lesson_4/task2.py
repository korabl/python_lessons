from random import randint

numbers = []
for i in range(15):
    n = randint(0, 100)
    numbers.append(n)

result = [el for el in numbers if el > numbers[numbers.index(el) - 1]]
print(numbers)
print(result)
