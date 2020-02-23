# task1
# from time import sleep
# from itertools import cycle
#
# class TrafficLight:
#     def __init__(self):
#         self._color = (('Red', 5), ('Yellow', 2), ('Green', 4))
#     def running(self):
#         for color, sec in cycle(self._color):
#             print(color, '(wait {} sec)'.format(sec))
#             sleep(sec)
#
# trafficLight = TrafficLight()
# trafficLight.running()

# task2
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def massa(self):
#         return self._length * self._width * 25 * 0.05
#
# myRoad = Road(20, 5000)
# print(myRoad.massa())

# task3
# incomeDict = {'wage': 20000, 'bonus': 5000}
#
# class Worker:
#     def __init__(self):
#         self.name = 'Name'
#         self.surname = 'Surname'
#         self.position = 'Manager'
#         self._income = incomeDict.values()
#
# employeer = Worker()
#
# class Position(Worker):
#     def getFullName(self):
#         print(f'{self.name} {self.surname}')
#     def getTotalIncome(self):
#         return sum(self._income)
#
# pos = Position()
# pos.getFullName()
# print(pos.getTotalIncome())

# task4
# class Car:
#     def __init__(self, speed, color, name):
#         self.speed = speed
#         self.color = color
#         self.name = name
#     def go(self):
#         print('Машина поехала')
#     def stop(self):
#         print('Машина остановилась')
#     def turn(self, direction):
#         print(f'Машина повернула {direction}')
#     def showSpeed(self):
#         print(f'Скорость {self.speed} км/ч')
#
# class TownCar(Car):
#     def showSpeed(self):
#         if self.speed > 60:
#             print('Скорость превышает 60 км/ч')
#
# class WorkCar(Car):
#     def showSpeed(self):
#         if self.speed > 40:
#             print('Скорость превышает 40 км/ч')
#
# myCar = Car(50, 'red', 'Toyota')
# myCar.go()
# myCar.stop()
# myCar.turn('направо')
# myCar.showSpeed()
#
# myWorkCar = WorkCar(60, 'blue', 'Prius')
# myWorkCar.go()
# myWorkCar.stop()
# myWorkCar.turn('налево')
# myWorkCar.showSpeed()

# task5
# class Stationary:
#     def __init__(self, title):
#         self.title = title
#     def draw(self):
#         print('Запуск отрисовки')
#     def titlePen(self):
#         print(self.title)
#
# class Pen(Stationary):
#     def draw(self):
#         print('Запуск ручной отрисовки')
#
# class Pencil(Stationary):
#     def draw(self):
#         print('Запуск карандашной отрисовки')
#
# class Handle(Stationary):
#     def draw(self):
#         print('Запуск маркерной отрисовки')
#
# myPen = Pen('ручка')
# myPen.draw()
# myPencil = Pencil('карандаш')
# myPencil.draw()
# myHandle = Handle('маркер')
# myHandle.draw()
#
# myPen.titlePen()
