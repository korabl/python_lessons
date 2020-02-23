from functools import reduce

def func(x, y):
    return x * y

myList = [el for el in range(100, 1001) if el % 2 == 0]
print(reduce(func, myList))