from itertools import count, cycle

# 1)
n = int(input('n: '))
for el in count(n):
    if el > 100: # специально ограничила бесконечность из задания до 100
        break
    print(el)

# 2)
myList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
с = 0
for el in cycle(myList):
    if с > 100:
        break
    print(el)
    с += 1