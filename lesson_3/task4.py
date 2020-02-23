# first
def my_func(x, y):
    return x ** y

result = my_func(int(input('x: ')), int(input('y: ')))
print(result)

# second
def my_func(x, y):
    i = 1
    z = x
    while i < y:
        z *= x
        i += 1
    return z

result = my_func(int(input('x: ')), int(input('y: ')))
print(result)