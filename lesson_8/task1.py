'''Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.'''

class Data:
    def __index__(self, str_data):
        self.str_data = str_data

    @classmethod
    def int_data(cls, param, type_data):
        res = param.split('-')
        if type_data == 'dd':
            res_data = int(res[0])
        elif type_data == 'mm':
            res_data = int(res[1])
        elif type_data == 'yy':
            res_data = int(res[2])
        else:
            print('Некорректный аргумент, введите dd, mm или yy')
        return res_data

    @staticmethod
    def valid_data(self):
        self.int_data()

example = '01-02-2019'
Data.int_data(example, 'yy')
Data.valid_data(example, 'yy')