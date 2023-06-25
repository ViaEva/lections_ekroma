# # # ООП(объектно ориентированное программирование) - цель создания была связать поведение объекта с ее данными

# # # Класс - это описание тоео, какими свойствами(данными) и поведением(функции) должен обладать объект(экземпляр).

# # # Объект - это экземпляр класса с собственным состоянием этих свойств 

# # # Свойствами называют обчные переменные(name+'John', height=185)

# # # Поведение это обычные функции(def eat- метод)

# # #=============================================================================

# # kirk= ['James Kirk',34,'Captain',2000]
# # snow = ['John Snow',28,'Police Officer',1500]
# # maccoy = ['Leonard Maccoy',30,'Chief',1800]

# # # for object in [kirk,snow,maccoy]:
# # #     print(f'Nmae: {object[0]}')
# # #     print(f'Age: {object[1]}')
# # #     print(f'Job: {object[2]}')
# # #     print(f'Salary: {object[3]}')
# # #     print()


# # # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# # # class work:
# # #     def __init__(self,name,age,work):
# # #         self.name = 'actor'
# # #         self.age = 'starik'
# # #         self.work = 'rabotyaga'

# # # maccoy = work('leonard',30,'chief')
# # # print(maccoy.name)
# # # //////////////////////////////////////////////////////////////////////////////


# # class Human:
# #     def __init__(self, name, age, job, salary):
# #         self.name = name
# #         self.age = age
# #         self.job = job 
# #         self.salary = salary
    
# #     def show_info(self):
# #         return f'Name: {self.name}\nAge: {self.age}\nJob: {self.job}\nSalary: {self.salary}\n'




# # kirk = Human('James Kirk',34,'Captain',2000)
# # snow = Human('John Snow',28,'Police Officer',1500)
# # maccoy = Human('Leonard Maccoy',30,'Chief',1800)

# # print(snow.name)
# # print(kirk.name)
# # print(maccoy.name)
# # print(Human,type(Human))
# # print()
# # print(maccoy.show_info())
# # print(kirk.show_info())
# # print(snow.show_info())

# # #=============================================================================

# # class Dog:
# #     ushi = True
# #     age = 0
    
# #     def __init__(self, name, color):
# #         '''
# #         Инициализаторю
# #         Именно здесь определяются аттрибуты
# #         объекта от класса
# #         '''

# #         # в self хронится сам объект 
# #         # атрибуты объекта
# #         self.name = name
# #         self.color = color

# # bobik = Dog('Bobik','brown')
# # yumi = Dog('Yumi','white')
# # ak_tosh = Dog('Ak tosh','black')

# # print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi {bobik.ushi}')
# # print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi {yumi.ushi}')
# # print(f'name: {ak_tosh.name}, age: {ak_tosh.age}, color: {ak_tosh.color}, ushi {ak_tosh.ushi}')

# # bobik.age = 3
# # yumi.age = 1
# # ak_tosh.age = 2
# # ak_tosh.ushi = False
# # print()

# # print(f'name: {bobik.name}, age: {bobik.age}, color: {bobik.color}, ushi {bobik.ushi}')
# # print(f'name: {yumi.name}, age: {yumi.age}, color: {yumi.color}, ushi {yumi.ushi}')
# # print(f'name: {ak_tosh.name}, age: {ak_tosh.age}, color: {ak_tosh.color}, ushi {ak_tosh.ushi}')


# # #=============================================================================

# # class Human:
# #     age = 0
    
# #     def __init__(self, name, weight, nationality):
# #         self.name = name
# #         self.weight = weight
# #         self.nationality = nationality

# #     def birthday(self):
# #         import random
# #         print(f'\nHappy birthday, {self.name} !!!!')
# #         self.age += 1
# #         self.weight += random.randint(3,7)

# # human1 = Human('John  Snow', 3.7, 'Aamerican')
# # human2 = Human('Abu-bakr', 3.1, 'Arabian')
# # print()
# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print()
# # print(human2.name, human2.age, human2.weight, human2.nationality)

# # print('After 5 month: ')
# # human1.birthday()
# # human2.birthday()

# # print()
# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print()
# # print(human2.name, human2.age, human2.weight, human2.nationality)      


# # print('After 1 year: ')
# # human1.birthday()


# # print()
# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print()
# # print(human2.name, human2.age, human2.weight, human2.nationality)



# # print('After 2 year: ')
# # human1.birthday()
# # human1.birthday()


# # print()
# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print()
# # print(human2.name, human2.age, human2.weight, human2.nationality)



# class Student:
#     univer = 'MIT'
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last = last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False

#     def add_point(self, point):
#         self.knowledge += point
#         if self.knowledge > 500:
#             self.is_ready_to_work = True
           
    
#     def read_book(self, book):
#         self.books.append(book)
#         self.add_point(50)
    
#     def do_lab_works(self):
#         self.add_point(50)

#     def do_real_project(self):
#         self.add_point(100)
    
#     def learn_new_language(self, language, point):
#         if not 60 < point <= 100:
#             raise Exception('Youre point out of range!!')
#         self.languages[language] = point
#         self.add_point(point)

# st1 = Student('John', 'Snow')
# st2 = Student('Jamie', 'Lanister')
# print(st1.name)
# print(st2.name)
# print(f'Before study {st1.name}: ', st1.books, st1.languages, st1.knowledge)
# print(f'Ready to work: {st1.is_ready_to_work}')

# st1.read_book('Game of Thrones')
# st1.read_book('Martin Iden')
# st1.read_book('Eugene Onegin')
# st1.read_book('War and Piece')

# st1.do_real_project()
# st1.do_lab_works()
# st1.do_real_project()
# st1.do_lab_works()

# st1.learn_new_language('Python',100)
# st1.do_real_project()
# st1.learn_new_language('Js',80)

# print(f'After study {st1.name}: ', st1.books, st1.languages, st1.knowledge)
# print(f'Ready to work: {st1.is_ready_to_work}')


"""
Напишите класс Salary для расчета налогов на заработную плату.
У класса должна быть обязательная переменная класса - процент налога от зарплаты - 15%.
Объекты класса должны иметь сумму зарплаты и стаж работы в качестве атрибутов.
Также у класса должен быть метод расчитывающий сумму налога заплаченного за весь стаж работы.
Создайте экземпляр класса и посчитайте сумму вашего налога.
"""

# class Salary:
#     tax = 0.15
#     def __init__(self, salary_, work_exp):
#         self.salary = salary_
#         self.wexp = work_exp
    
#     def summ(self):
#         return (self.salary*self.tax)*12*self.wexp

# obj = Salary(8000,2)
# print(obj.summ())









# class PythonCourse:
#   def __init__(self, key, value):
#     self.key = key
#     self.value = value
    
#   def learn(self, a):
#     a.setdefault(self.key, self.value)
#     print(a)

# a = {1: 'OOP basics', 2: 'Inheritance', 3: 'Polymorphism', 4: 'Encapsulation'}

# dik = PythonCourse(5, 'Abstraction')
# dik.learn(a)


# class Hogwarts:
#   Gryffindor = []
#   Ravenclaw = []
#   Hufflepuff = []
#   Slytherin = []

#   def __init__(self,name, courage, intelligence, justice, ambition):
#     self.name = name
#     self.courage = courage
#     self.intelligence = intelligence
#     self.justice = justice
#     self.ambition = ambition

#   def sorting_hat(self):
#     res = sorted([self.courage, self.ambition, self.intelligence, self.justice])
#     if res[-1] == self.justice:
#       self.Hufflepuff.append(self)
#       print(f'{self.name} вступил в Hufflepuff')
#     elif res[-1] == self.courage:
#       self.Gryffindor.append(self)
#       print(f'{self.name} вступил в Gryffindor')
#     elif res[-1] == self.intelligence:
#       self.Ravenclaw.append(self)
#       print(f'{self.name} вступил в Ravenclaw')
#     else:
#       self.Slytherin.append(self)
#       print(f'{self.name} вступил в Slytherin')
 

    
# student1 = Hogwarts('potter',100,40,50,20)
# student2 = Hogwarts('malfoy',10,30,50,100)
# student3 = Hogwarts('grim',40,100,50,20)
# student4 = Hogwarts('daniel',60,40,90,20)

# student1.sorting_hat()
# student2.sorting_hat()
# student3.sorting_hat()
# student4.sorting_hat()

# print(student1.Gryffindor)
# print(student2.Ravenclaw)
# print(student3.Hufflepuff)
# print(student4.Slytherin)


# Множественное наследование - Это когда класс наследуется от двух или более классов 

# class A:
#   lol = 1

# class B(A):
#   lol = 2                                                
#   pass

# class C(A):
#   # lol = 3
#   pass

# class D(B,C):
#   def o(self):
#     print(self.lol)

# l = D()
# l.o()

# class Zero:
#   def say(self):
#     print('Class zero')
  
# class First:
#   pass





# class Y:
#   pass

# class X:
#   pass

# class A(X,Y):
#   pass

# class B(Y,X):
#   pass

# class C(A,B):
#   pass

# class Machines:
#   def starts():
#     pass
  

