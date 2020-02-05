x = int(input('Input x: '))
y = int(input('Input y: '))

def delete(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('На ноль делить нельзя')
    return result

print(delete(x, y))