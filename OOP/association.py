# #  Ассоциация, Компазиция, Агрегация
# # Все эти три принципа очень похожи друг на друга. Все они означают что внутри одного объекта будет существовать другой.



# # Компазиция 

# # class Wall:
# #     def __init__(self, direction) -> None:
# #         self.type = direction

# #     def __str__(self) -> str:
# #         for i in self.type:
# #             print(i)
# #         return self.type

# # class Room:
# #     def __init__(self):
# #         self.west_wall = Wall('west')
# #         self.east_wall = Wall('east')
# #         self.south_wall = Wall('south')
# #         self.north_wall = Wall('north')

# # room = Room()
# # print(room.west_wall)



# # Ассоциации

# # class Stream:
# #     def __str__(self) -> str:
# #         return 'John\'s stream'

# # class Logger:
# #     def __init__(self) -> None:
# #         self.stream = None

# #     def print_the_string(self):
# #         if self.stream:
# #             print(f'Stream from class: {self.stream}')
# #         else:
# #             print('None stream')

# # logger = Logger()
# # logger.stream = Stream()
# # logger.print_the_string()
# # logger.stream = Stream()


# # Агригация

# # class Stream:
# #     def __str__(self) -> str:
# #         return 'John\'s stream'

# # class Logger:
# #     def __str__(self) ->str:
# #         print(self)

# #     def print_the_string(self):
# #         if self.stream:
# #             print(f'Stream from class: {self.stream}')
# #         else:
# #             print('None stream')

# # stream = Stream()
# # logger = Logger(stream)
# # logger.print_the_string()

# # class Engine:
# #     country = 'Germany'
# #     def __init__(self, power) -> None:
# #         self.power = power

# #     def __str__(self) -> str:
# #         return f'Country: {self.country} -> Engine: {self.power}'

# # class Car:
# #     model = 'Audi'
# #     country = 'Germany'

# #     def __init__(self, type, power):
# #         self.engine = Engine(power)
# #         self.type = type

# #     def __str__(self) -> str:
# #         return f'{self.model} {self.type} -> Engine: {self.engine} -> Country {self.country}'

# # car = Car('A8', 360)
# # print(car)

# ###################################################################################################


# # class methods, instance methods, static methods

# # Методы экземпляра класса (instance methods) - это те методы в ООП которые изменяют состояние экземпляра класса:

# # def method(self) - self сылка на экземпляр

# # Методы класса (class methods) - это те методы которые могут изменять состояние самого класса и манипулировать самим классом:
# # @classmethod -- декоратор который определяет метод класса 
# # def method(cls) -- cls это ссылка на сам класс

# # Статические методы(Static methods) - это те методы которые не могут изменять состояние ни экземпляра от класса ни самого класса:
# # @staticmethod   Декоратор который определяет статик метод
# # def method(self):



# # class Student:
# #     shool_name = 'ABC school'

# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
        
# #     def show(self):
# #         print(self.name, self.age, 'School: ', Student.shool_name)

# #     @classmethod
# #     def change_school(cls,name):
# #         print('!!!',cls)
# #         print('!!!',Student)
# #         # class_name.class_variable
# #         cls.shool_name = name

# # john = Student('John',20)
# # john.show()
# # john.change_school('xyz School')
# # john.show()


# #####################################################################

# class Person:
#     surname = 'snow'

#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     @staticmethod
#     @classmethod
#     def is_adult(cls, age):
#         if age >= 18:
#             print('Person is adult')
#         else: print('Person is not adult')

# john = Person('john', 24)
# print(john.name, john.surname)
# Person.is_adult(john.age)
# john.is_adult(17)
