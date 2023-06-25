# # Инкапсуляция: 
# # 1. Связь данных с методами которые должны упровлять этими данными
# # 2. Механизм языка, который позволяет ограничить доступ одних компонентов программы к другим 

# # Инкапсуляция как связь
# # class Phone:
# #     number = '+996 123 123 123'

# #     def print_number(self):
# #         print(f'Мой номер{self.number}')

# # my_phone = Phone()
# # my_phone.print_number()

# # Инкапсуляция как упровление доступом
# # 3 Уровня доступа в питоне:
#     # 1. Публичный  (public) - number
#     # 2. Защщищенный(_protected, parent/child) - _number
#     # 3. Приватный  (__private, частный, только в текущем классе) = __number

# # class Car:
# #     country = 'germany'
# #     def __init__(self):
# #         self.marka = 'Honda' #public
# #         self._model = 'Fit' #protected
# #         self.__motor = 'Abc' #private

# #     def _get_date(self): #protected
# #         print('1 september')
# #         print('ito:',self.__motor)

# # class Audi(Car):
# #     def _get_date(self):
# #         print(self.__motor)

# # class Auto(Audi):
# #     pass

# # audi = Audi()
# # print(audi.marka)
# # print(audi._model)
# # audi._get_date()
# # auto = Auto()
# # print(auto.marka)
# # print(auto._model)
# # auto._get_date()

# # car = Car()
# # print(car.marka)
# # print(car._model)
# # # print(car.__motor)
# # car._get_date()
# # car.marka = 'BMW'
# # car._model = "x7"
# # car.__motor = 'BBC'
# # print(car.marka)
# # print(car.__motor)
# # car._get_date()


# # class Phone:
# #     username = 'John'
# #     _caller = 'Stark'
# #     __count_of_calls = 15

# # phone = Phone()
# # print(phone.username)
# # print(phone._caller)
# # # print(phone.__count_of_calls)
# # print(phone._Phone``__count_of_calls)

# # getter & setter
# # они используюутся для получения и установки значений, чтобы добавить логику проверки при получении данных 
# #  Еще чтобы избежать прямого допступа к защищенному полю класса 

# # class Person:
# #     def __init__(self, name):
# #         self.name = name
# #         self.age = 0

# #     def display_info(self):
# #         print(f'My name is {self.name}, and i`m {self.age} years old')

# # john = Person('John')
# # john.display_info()
# # john.name = 'jamie'
# # john.age = 18
# # john.display_info()
# # john.age = -18
# # john.name = None
# # john.display_info()

# # class Person:
# #     def __init__(self, name):
# #         self.__name = name
# #         self.__age = 0
    
# #     def display_info(self):
# #         print(f'My name is {self.__name}, and i`m {self.__age} years old')

# #     def get_name(self): return self.__name
# #     def set_name(self, name):
# #         if not isinstance(name, str):
# #             raise Exception('InvalidValue attribute for name')
# #         self.__name = name
# #     def get_age(self): return self.__age
# #     def set_age(self, age):
# #         if not isinstance(age, int) or age < 0:
# #             raise Exception('InvalidValue attribute for age')
# #         self.__age = age
    
# # john = Person()
# # john.display_info()
# # print(john.get_name())
# # john.set_name('jamie')
# # print(john.get_name())
# # print(john.get_age())
# # john.set_age(28)
# # print(john.get_age())


# """
# Анотации свойств(@property(getter setter)
# """

# class Person:
#     __name = 'John'
#     __age = 22
    
#     @property
#     def name(self):
#         'getter'
#         return self.__name
    
#     @name.setter
#     def name(self, value):
#         print('setter')
#         if not isinstance(value, str):
#             raise Exception('Invalid Value')
#         self.__name = value 
#     def age():
#         def age(self):
#             return self.__age

#         @age.setter 
#         def age(self, age):
#             if not isinstance(age, (int, float)) or not 0 < age < 170:
#                 raise Exception('Invalid Value')
#             self.__age = age
        
# john = Person()
# print(john.name)
# john.name = "Jonas"
# print(john.name)
# john.age = 18

# print(john._Person__age)

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     def _get_radius(self):
#         print('Getter')
#         return self._radius

#     def _set_radius(self, value):
#         print('Setter')
#         self._radius = value

#     def _del_radius(self):
#         print('Deletter')
#         del self._radius

#     radius = property(fget=_get_radius,fset=_set_radius,fdel=_del_radius,doc='The protected radius property ')

# circle = Circle(42)
# print(circle.radius)

# circle.radius = 100
# print(circle.radius)

# del circle.radius


# class Car:
#     def __init__(self, model):
#         self.__model = model

#     model = property(lambda self: self.__model)

# bmw = Car('BMW')
# mers = Car('MERS')

# print(bmw.model)
# print(mers.model)

# # read only

# class CoordinateWriteError(Exception):
#     pass

# class Point:
#     def __init__(self, x, y) -> None:
#         self._x = x
#         self._y = y

#     @property
#     def x(self):
#         return self._x
    
#     @property
#     def y(self):
#         return self._y

#     @x.setter
#     def x(self, value):
#         raise CoordinateWriteError('x coordinate is read only')

#     @y.setter
#     def y(self, value):
#         raise CoordinateWriteError('y coordinate is read only')

# point = Point(15,5)
# print(point.x)
# print(point.y)

# point.x = 12
# print(point.x)
# #  >>>> cant set attribut

# class Circle:
#     def __init__(self, radius):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         self._radius = value

#     @property
#     def diameter(self):
#         return self._radius * 2

#     @diameter.setter
#     def diameter(self, value):


# import hashlib
# import os

# class User:
#     def __init__(self, name, password):
#         self.username = name
#         self.password = password

#     @property
#     def password(self):
#         raise AttributeError('Password is write-only')

#     @password.setter
#     def password(self, password):
#         salt = os.urandom(32)
#         self._hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000)

# john = User('john','secretkey')
# # print(john.password)
# john.password = '12345qwerty'
# print(john._hashed_password)


# class Shape:
#     def get_area(self):
#         pass

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base  = base 
#         self.height = height

#     def get_area(self):
#         return 1/2 *self.base*self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return 3.14*self.radius**2


# class Square(Shape):
#     def __init__(self, length):
#         self.length = length 

#     def get_area(self):
#         return self.length**2

# triangle = Triangle(6,3)
# square = Square(4)
# circle = Circle(5)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area()) 

# from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
    
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height

#     def get_area(self):
#         return 1 / 2 * self.base * self.height

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         return self.length**2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pi * self.radius**2

# triangle = Triangle(6, 3)
# square = Square(4)
# circle = Circle(5)

# print(triangle.get_area()) 
# print(square.get_area()) 
# print(circle.get_area())




# class A:
#     def __init__(self, param):
#         pass

# class B(A):
#     pass

# class C(A):
#     pass

