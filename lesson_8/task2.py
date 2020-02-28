''' Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''

class MyError(Exception):
    def __init__(self, text):
        self.txt = text

a = input("х: ")

try:
    a = int(a)
    if a == 0:
        raise MyError("Деление на ноль")
    res = 100/a
except ValueError:
    print("Неккоректный ввод")
except MyError as mr:
    print(mr)
else:
    print(res)
