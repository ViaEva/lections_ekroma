# class Cat:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f' Its a cat: Cats name is {self.name} , age is {self.age}')
    
#     def make_sound(self):
#         print('Meow, meow')


# class Dog:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f' Its a dog: dogs name is {self.name} , age is {self.age}')

#     def make_sound(self):
#         print('Bark, bark')

# cat = Cat('Garfield', 3)
# dog = Dog('Pluto', 9)

# for i in (cat,dog):
#     i.info()
#     i.make_sound()


# class Shape:
#     def __init__(self, name):
#         self.name = name 

#     def area(self):
#         pass

#     def fact(self):
#         return 'Я фигура в двумерной плоскости'

#     def __str__(self) ->str:
#         return self.name

# class Square(Shape):



# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня
# заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 0,5 %
# заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность заряжания батареи.

# class Phone:
#     _charge = 100
#     def __init__(self, imei,os):
#         self._imei = imei
#         self._os = os
    
#     def check_charge(self,a):
#         if self._charge <= a:
#             self._charge = 0
#             raise Exception('телефон разряжен')
        
#     def data(self):
#         self.check_charge(0)
#         print('вы открыли хранилище файлов')
#         self._charge -= 0.5

#     def music(self):
#         self.check_charge(0)
#         print('Вы прослушали музыку')
#         self._charge -= 5
#         self._charge -= 0.5

#     def video(self):
#         if self._charge > 6:
#             print('Вы посмотрели игру пристолов')
#             self._charge -= 7
#             self._charge -= 0.5
#         else:
#             print('телефон разряжен')

#     def zaryad(self):
#         self._charge = 100
#         print('телефон заряжен')

#     def info(self):
#         self.check_charge(0)
#         print(f'charge: {self._charge}, os: {self._os}, imei: {self._imei} ')
#         self._charge -= 0.5

# tel = Phone(input('Введите imei:'),input('Введите os:'))

# while 1 != 0:
#     i = input('1 - data, 2 - music, 3 - video, 4 - zaryadka, 5 - charge')
#     if i == '1':
#         tel.data()
#     elif i == '2':
#         tel.music()
#     elif i == '3':
#         tel.video()
#     elif i == '4':
#         tel.zaryad()
#     elif i == '5':
#         tel.info()
#     else:
#         print('tokogo net')


from time import localtime

print(localtime())