numbers = [1, 2, 55, 1, 0, 0, 32, 55, 32, 11, 2, 12, 8, 6, 6]
result = [el for el in numbers if numbers.count(el) == 1]
print(result)
