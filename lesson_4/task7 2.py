import math

def gen():
    for el in range(100):
        yield el

i = 0
for el in gen():
    if i < 15:
        f = math.factorial(el)
        print(f)
    i += 1

