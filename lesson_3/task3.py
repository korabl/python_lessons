def my_func(x, y, z):
     return ((x + y + z) - min(x, y, z))

result = my_func(int(input('x: ')), int(input('y: ')), int(input('z: ')))
print(result)