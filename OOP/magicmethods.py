# magic methods
# dunder methods -(double uderscore) - __init__
# служебные методы

# res = 5 + 5  #__add__
# print(res)

# class A(int):
#     pass

# obj = A()
# print(dir(obj))


# __le__(self, other) -> <=

# __ge__(self, other) -> <=

# class Word(str):
#     def __init__(self, word) -> None:
#         self.word = word
    
    # def __gt__(self, __x: str) -> bool:
    #     print('gt сработал')
    #     return len(self) > len(__x)

#     def __lt__(self, other:str) -> bool:
#         print('lt сработал')
#         return len(self) < len(other)

#     # def lt(self, other):
#     #     print('lt сработал')
#     #     return len(self) < len(other)

# obj = Word('Hello')
# obj1 = Word('courses')
# print(obj > obj1)
# print(obj < obj1)


# class MyTuple:
#   def __init__(self, *args) -> None:
#     self.ls = args

#   def __res__(self, __x:int):
#     print('dede')
#     return sum(self)


# m1 = MyTuple(1,2,3)
# print(m1)
# --------------------------------------------

# конструктор -> __new__
# Инициализатор -> __init__

# class Conventer(float):
#     def __new__(cls, x):
#         print('New  сработал!!!')
#         print('!!!', cls)
#         print('xxx', x)
#         if x < 50:
#             raise ValueError
#         return super().__new__(cls, x)

#     def __init__(self, number) -> None:
#         print('---', self)
#         self.number = number

# obj = Conventer(100.0)
# print(obj.number)


# class Human:
#     def __new__(cls, stroka):
#         x = 'stroka' + stroka + '!!!'
#         return 'stroka' + stroka

#     def __init__(self, stroka):
#         self.stroka = stroka

# obj = Human('Alpha')
# obj1 = Human('Omega')
# print(obj)
# print(obj1)
# print(obj.stroka)
# print(obj1.stroka)


#  ---------------------

# Дандер методы для строкового отображения объектов

# __str__ -> для отображения строки, которую будут вилеть ползователи

#__repl__ -> строковую информайию как создовать экземпляр от класса

# class Base:
#     def __init__(self, stroka) -> None:
#         self.stroka = stroka

#     def __str__(self) -> str:
#         return f' Объект: {self.stroka}'

#     def __repr__(self) -> str:
#         return f'Base("{self.stroka}")'
# word = Base('Hello John')
# print(word)
# print(repr(word))
# word3 = eval(repr(word))
# print(word3)

# class User:
#     def __init__(self, name, email) -> None:
#         self.name = name 
#         self.email = email

#     def __str__(self) -> str:
#         return f'{self.name} -> {self.email}'

# user = User('Jasy', 'Jasy00123@email.com')
# print(user)

#-------------------------------
# + - / * // % **

# class Cifra(int):
#     def __new__(cls, number):
#         print('vyzov new')
#         instace = super().__new__(cls)
#         if not 0 < number < 100:
#             raise ValueError('Введите число от 0 до 100')
#         return instace

#     def __init__(self, number) -> None:
#         self.number = number

#     def __add__(self, other):
#         print('add вызван')
#         print(f'Result: {self} + {other} - {self.number + other.number}')

# cif = Cifra(11)
# cif2 = Cifra(56)
# cif + cif2
# cif + cif2

# # __sub__ -> - 
# # __mul__ -> *
# # __floordiv__ -> //
# # __div__ -> /
# # __mod__ -> %
# class ZwezdaMixin:
#     def zwezda(self, slovo):
#         res = '*' * (len(slovo) -1)
#         return slovo[0] + res
        

# class MyUser(ZwezdaMixin):
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last = last_name

#     def __str__(self) -> str:
#         return f'{self.zwezda(self.name)} {self.zwezda(self.last)}'

#     def __password(self) ->str:
#         pass


# s = MyUser('hello', 'World')
# print(s)


# class ZwezdaMixin:
#   def zwezda(self, slovo):
#     res = '*' * (len(slovo) -1)
#     return slovo[0] + res
        
# class PasswordMixin:
#   def pass_gen(self, name, last):
#     res = []
#     for v in last, name:
#         for i in v:
#             if i in 'aeuoiy':
#                 res.append(i)
#     return ''.join(res)

# class MyUser(ZwezdaMixin, PasswordMixin):
#   def __init__(self, name, last_name):
#     self.name = name
#     self.last = last_name
#     self.password = self.pass_gen(name, last_name)
#     if self.password:
#         raise Exception('Forbiden')
#   def __str__(self) -> str:
#     return f'{self.zwezda(self.name)} {self.zwezda(self.last)}'

# s = MyUser('hello', 'World')
# print(s.password)


# def pass_gen(name, last):
#     res = []
#     for v in name,last:
#         for i in name:
#             if i in 'aeuoiy':
#                 res.append(i)
#     return ''.join(res)

# print(pass_gen('ololedad', 'edader'))

# class ZwezdaMixin:
#   def zwezda(self, slovo):
#     res = '*' * (len(slovo) -1)
#     return slovo[0] + res
        
# class PasswordMixin:
#   def pass_gen(self, name, last):
#     res = []
#     for v in last, name:
#         for i in v:
#             if i in 'aeuoiy':
#                 res.append(i)
#     return ''.join(res)

# class MyUser(ZwezdaMixin, PasswordMixin):
#   def __init__(self, name, last_name):
#     self.name = name
#     self.last = last_name
#     self.password = self.pass_gen(name, last_name)
#     if self.password:
#         raise Exception('Forbiden')
#   def __str__(self) -> str:
#     return f'{self.zwezda(self.name)} {self.zwezda(self.last)}'

# s = MyUser('hello', 'World')
# print(s)




# class User:
#   def __init__(self, name):
#     self.name = name

#   def __call__(self):
#     print(self.name)
#     self.hello = 'Hello world'

# us = User('John')
# # us()
# print(us.hello)

#-____________________________________________-

# class LogSetFile:
#   def __init__(self, file):
#     self.file = file

#   def __call__(self, func):
#     def wrapper(*args, **kwargs):
#       with open(self.file, 'a') as file:
#         file.write(f'Func name: {self.__name__}\n')
#       return func(*args, **kwargs)
#     return wrapper

# test = LogSetFile('text.txt')
# print(callable(test))

# @test
# def start_test():
#   pass

# @test
# def hello():
#   pass

# @test
# def hello():
#   pass

# # start_test()
# test(start_test)

# class Student(dict):
#   def __init__(self, bally):
#     self.bally = bally
#     self.avg_res = sum([v for v in self.bally.values()]) / len(self.bally)
  
#   def __gt__(self, other) -> bool:
#     print('gt сработал')
#     return sum(self.bally.values()) / len(self.bally) > sum(other.bally.values()) / len(other.bally)

# john = Student({'math': 100, 'history': 95, 'literature': 75})
# jamie = Student({'math': 93, 'history': 100, 'literature': 85})


# print(john < jamie)


# class Kopilka:
#   def __init__(self) -> None:
#     self.__total = 0
#     self.__coins = []

#   def add_coin(self, coin):
#     self.__total += coin
#     self.__coins.append(coin)

#   @property
#   def total(self): return self.__total

#   def __len__(self):
#     return len(self.__coins)

#   def __getitem__(self, index):
#     return self.__coins[index]


# obj = Kopilka()
# obj.add_coin(25)
# obj.add_coin(30)
# obj.add_coin(55)
# obj.add_coin(10)
# print(len(obj))
# print(obj.total)

# for i in obj:
#   print(i)



# class Car:
#   def __init__(self):
#     self.model = 'Honda'

#   def __delattr__(self, name):
#     value = getattr(self, name)
#     print(f'{value} removed')
#     super().__delattr__(name)

# honda = Car()
# print(honda.model)

# del honda.model

# print(honda.model)


# class Person:
#   def __init__(self, attrs):
#     for k,v in attrs.items():
#       setattr(self, k, v)

# alice = Person({'name': 'Alice Rose', 'income': 10000, 'eyes': 'brown'})
# john = Person({'email': 'JohnSnow@gmail.com', 'last_name': 'Snow'})
# print(type(int))
