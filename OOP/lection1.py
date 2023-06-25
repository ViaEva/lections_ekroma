#############    ООП: Введение    #############

'''
Объектно-ориентированное программирование основано на парадигме императивного программирования, которая использует операторы для изменения состояния программы. Основное внимание уделяется описанию того, как должна работать программа. Примерами императивных языков программирования являются C, C ++, Java, Go, Ruby и Python. Это противоречит декларативному программированию, в котором основное внимание уделяется тому, что должна выполнять компьютерная программа, без указания как. Примерами являются языки запросов к базе данных, такие как SQL и XQuery, где только компьютер сообщает, какие данные откуда запрашивать, а теперь как это сделать.

ООП использует концепцию объектов и классов. Класс можно рассматривать как «чертеж» для объектов. Они могут иметь свои собственные атрибуты (характеристики, которыми они обладают) и методы (действия, которые они выполняют).

Примером класса является класс Dog. Не думайте об этом как о конкретной собаке или о своей собственной собаке. Мы описываем, что собака вообще может делать. Собаки обычно имеют name и age - это атрибуты экземпляра. Собаки могут также лаять (bark) - это метод.

Когда вы говорите о конкретной собаке, это у вас будет объект в программировании: объект является экземпляром класса. Это основной принцип, на котором основано объектно-ориентированное программирование. Так, например, моя собака Ак-Тош принадлежит к классу Dog. Его атрибутами будут name = 'Ak-Tosh'и age = '2'. У другой собаки будут другие атрибуты.

Как создать класс.
Чтобы определить класс в Python, вы можете использовать ключевое слово class, за которым следует имя класса и двоеточие. Внутри класса метод __init__ должен быть определен с def. Это инициализатор, который вы позже сможете использовать для создания экземпляров класса. Это похоже на конструктор в Java. Ему требуется один обязательный параметр: self, который относится к самому объекту. Внутри метода на данный момент используется ключевое слово pass, потому что Python ожидает, что вы что-то там напечатаете. 
'''

# class Dog:

#     def __init__(self):
#         pass

'''
Таким образом у вас есть класс Dog, но еще нет объекта. Давайте создадим один!

Создание объектов.
Чтобы создать экземпляр от класса, введите имя класса, а затем две скобки. Вы можете присвоить это переменной, чтобы в дальнейшем отслеживать объект.
'''

# ak_tosh = Dog()
# print(ak_tosh)
# # <__main__.Dog object at 0x111f47278>

'''
Добавление атрибутов в класс.
После печати ak_tosh становится ясно, что этот объект - собака. Но вы еще не добавили никаких атрибутов. Давайте дадим Dog классу имя и возраст, переписав его:
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

'''
Вы можете видеть, что функция теперь принимает два аргумента после self: name и age. Затем они назначаются self.name и self.age соответственно. Теперь вы можете создать новый объект ak_tosh с именем и возрастом:
'''

# ak_tosh = Dog("Ak-Tosh", 2)

'''
Чтобы получить доступ к атрибутам объекта в Python, вы можете использовать точечную запись. Это делается путем ввода имени объекта, затем точки и имени атрибута.
'''

# print(ak_tosh.name)
# print(ak_tosh.age)
# # Ak-Tosh
# # 2

'''
Это также может быть объединено в более сложное предложение:
'''

# print(ak_tosh.name + " is " + str(ak_tosh.age) + " year(s) old.")
# # Ak-Tosh is 2 year(s) old.
# # Функция str() используется здесь , чтобы преобразовать age атрибут, который представляет собой целое число, в строку.

'''
Определите методы в классе.
Тепер у вас есть класс Dog, у которого есть имя и возраст, которые вы можете отслеживать, но он ничего не делает. Вот тут-то и появляются методы экземпляра. Перепишите класс, чтобы включить метод bark(). Обратите внимание, как снова используется ключевое слово def, а также аргумент self.
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

'''
Теперь метод bark можно вызывать с помощью точечной нотации после создания нового объекта ak_tosh. Метод должен печатать "gav gav!" на экран. Обратите внимание на круглые скобки в .bark(). Они всегда используются при вызове метода. В этом случае они пусты, поскольку метод bark() не принимает никаких аргументов.
'''

# ak_tosh = Dog("Ak-Tosh", 2)

# ak_tosh.bark()
# # gav gav!

'''
Вспомните, как вы печатали ak_tosh ранее? Код ниже теперь реализует эту функциональность в классе Dog с помощью метода doginfo(). Затем вы создаете еще несколько экземпляров с разными свойствами и вызываете для них метод.
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

# ak_tosh = Dog("Ak-Tosh", 2)
# rex = Dog("Rex", 12)
# bobik = Dog("Bobik", 8)
# ak_tosh.doginfo()
# rex.doginfo()
# bobik.doginfo()
# # Ak-Tosh is 2 year(s) old.
# # Rex is 12 year(s) old.
# # Bobik is 8 year(s) old.

'''
Как видите, вы можете вызывать метод doginfo() для объектов с помощью точечной нотации. Ответ теперь зависит от того, для какого объекте Dog вы вызываете метод.

Поскольку собаки становятся старше, было бы неплохо, если бы вы могли соответствующим образом скорректировать их возраст. Ак-Тош только что исполнилось 3 года, поэтому давайте изменим его возраст.
'''

# ak_tosh.age = 3
# print(ak_tosh.age)
# # 3

'''
Это так же просто, как присвоить новое значение атрибуту. Вы также можете реализовать это как метод birthday() в классе Dog:
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1

# ak_tosh = Dog("Ak-Tosh", 2)
# print(ak_tosh.age)
# # 2
# ak_tosh.birthday()
# print(ak_tosh.age)
# # 3

'''
Теперь вам не нужно вручную менять возраст собаки. Когда у него день рождения, вы можете просто вызвать метод birthday().

Передача аргументов в методы.
Вы хотели бы, чтобы у наших собак был приятель. Это должно быть необязательным, так как не все собаки общительны. Взгляните на метод setBuddy() ниже. Он принимает self, как обычно, и buddy в качестве аргументов. В этом случае buddy будет еще один объект от класса Dog. Установите для self.buddy атрибута значение buddy, а для buddy.buddy атрибута - self. Это означает, что отношения взаимны; ты приятель своего приятеля. В этом случае Ак-Тошу будет приятелем Рекс, а это означает, что Рекс автоматически становится приятелем Ак-Тошу. Вы также можете установить эти атрибуты вручную, вместо определения метода, но это потребует дополнительной работы (написание 2 строк кода вместо 1) каждый раз, когда вы хотите назначить приятеля. 
'''

# class Dog:

#     def __init__(self, name, age):  
#         self.name = name
#         self.age = age

#     def bark(self):
#         print("gav gav!")

#     def doginfo(self):
#         print(self.name + " is " + str(self.age) + " year(s) old.")

#     def birthday(self):
#         self.age +=1

#     def setBuddy(self, buddy):
#         self.buddy = buddy
#         buddy.buddy = self

'''
Теперь вы можете вызвать метод с точечной нотацией и передать ему другой объект от класса Dog. В этом случае приятелем Ак-Тоша будет Рекс:
'''

# ak_tosh = Dog("Ak-Tosh", 2)
# rex = Dog("Rex", 8)

# ak_tosh.setBuddy(rex)

'''
Если вы сейчас хотите получить какую-нибудь информацию о приятеле Ак-Тоша, вы можете использовать точечную запись дважды. Во-первых, чтобы сослаться на приятеля Ак-Тоша, и во второй раз, чтобы сослаться на его атрибут.
'''

# print(ak_tosh.buddy.name)
# print(ak_tosh.buddy.age)
# # Rex
# # 8

# # Обратите внимание, как это можно сделать для Рекса.

# print(rex.buddy.name)
# print(rex.buddy.age)
# # Ak-Tosh
# # 2

'''
Методы приятеля также могут быть вызваны.
'''

# ak_tosh.buddy.doginfo()
# # Rex is 8 year(s) old.

'''
Теперь вы знаете, как объявлять классы и методы, создавать экземпляры классов, устанавливать их атрибуты и вызывать методы экземпляров. 

С ООП ваш код будет усложняться по мере увеличения вашей программы. У вас будут разные классы, подклассы, объекты, наследование, методы экземпляра и многое другое. Для того, чтобы ваш код был правильно структурирован и читабелен, рекомендуется следовать шаблонам проектирования.
'''

# class Soda:
#     def __init__(self, ingredient=None):
#         if isinstance(ingredient, str):
#             self.ingredient = ingredient
#         else:
#             self.ingredient = None

#     def show_my_drink(self):
#         if self.ingredient:
#             print(f'gazirofka iz {self.ingredient}')
#         else:
#             print('normal  gazirovka')

# drink1 = Soda('malina')
# drink1.show_my_drink()
# drink2 = Soda(5)
# drink2.show_my_drink()

# class TriangleChecker:
#     def __init__(self,sides):
#         self.sides = sides
    
#     def isTriangle(self):
#         if any(type(side) == bool for side in self.sides):
#             return 'Нужно вводить только числа!'
#         if not all (isinstance(side, (int, float)) for side in self.sides):
#             return 'Нужно вводить только числа.'
#         if not all (side > 0 for side in self.sides):
#             return('Числа должны быть больше нуля!')
#         sorted_sides = sorted(self.sides)
#         if sorted_sides[0] + sorted_sides[1] < sorted_sides[2]:
#             return 'С этими сторонами нельзя сделать треульник!'
#         return f'Да, мы можем построить треугольник с данными отрезками - {self.sides}'

# triangle1 = TriangleChecker([77,3,4])
# print(triangle1.isTriangle())
# t1 = TriangleChecker([2,3,'otrk'])
# print(t1.isTriangle())
# t2 = TriangleChecker([2,3,-4])
# print(t2.isTriangle())
# t3 = TriangleChecker([2,3,1])
# print(t3.isTriangle())
# t4 = TriangleChecker([2,3,4])
# print(t4.isTriangle())



# class Employee:
#     bonus = 1.5
   
#     def __init__(self, name, last_name, salary):
#         self.name = name
#         self.last_name= last_name
#         self.salary = salary

#     def get_full_name(self):
#         return f'{self.name} {self.last_name}'

#     def give_bonus(self):
#         self.salary = self.salary * self.bonus

# class Developer(Employee):
#     def __init__(self, name, last_name, salary, prog_lang):
#         super().__init__(name, last_name, salary)
#         self.lang = prog_lang

# class Manager(Employee):
#     def __init__(self, name, last_name, salary, emps=None):
#         super().__init__(name, last_name, salary)
#         if emps == None:
#             self.emps = []
#         else:
#             self.emps = emps
#     def add_emp(self, emp):
#         if emp not in self.emps:
#             self.emps.append(emp)
#             print(emp,'is in')
#         else:
#             print('Employee already is in')

#     def show_emps(self):
#         result = []
#         for emp in self.emps:
#             result.append(emp.get_full_name())
#         return result

# dev1 = Developer('john', 'snow', 1500, 'python')
# dev2 = Developer('Steve', 'Woznik', 2000, 'JS')
# dev3 = Developer('Lary', 'Page', 3000, 'python')
# dev4 = Developer('Jamie', 'Lanister', 1500, 'JS')

# man1 = Manager('Ivan', 'Ivanov',3000)
# man2 = Manager('Dastan', 'Velikiy', 4000, emps=[dev1,dev2])

# man1.add_emp(dev3)
# man1.add_emp(dev4)
# man1.add_emp(dev3)

# print(man1.get_full_name())
# print(man1.show_emps())
# print(man2.get_full_name())
# print(man2.show_emps())

# man2.give_bonus()
# man2.add_emp(dev3)

# print(f'Manager {man1.get_full_name()} has {man1.show_emps()} developers, his salary {man1.salary}')
# print(f'Manager {man2.get_full_name()} has {man2.show_emps()} developers, his salary {man2.salary}')
# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(f'Hello, my name is {self.name}, and I`m {self.age} years old')

# class Student(Person):
#     def __init__(self, name, age, univer):
#         super().__init__(name, age)
#         self.univer = univer

#     def info(self):
#         super().info()
#         print(f'i study at {self.univer}')


# mike = Student("Mike",20,"auca")
# mike.info()
# print(mike.name)        


# /////////////////////////////////////////////////




# class Post:
#     id = 0
#     def __init__(self, user):
#         self.user = user
#         self.posts = []

#     # CRUD
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status ': 201, 'msg':'successfully created'}

#     def retrieve_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 return {'status': 200, 'content': post}
#         return {'status':404,'msg':'Not found'}

#     def update_post(self, post_id, **kwargs):
#         for post in self.posts:
#             if post['id'] == post_id:
#                 index = self.posts.index(post)
#                 self.posts[index].update(**kwargs)
#                 post.update(**kwargs)
#                 return {'status': 200, 'msg':'updated'}
#         return {'status': 404, 'msg': 'not founf'}

#     def delet_post(self, post_id):
#         for post in self.posts:
#             if post.get('id') == post_id:
#                 self.posts.remove(post)
#                 return {'status':204, 'msg':'No content found'}


# acc1 = Post('JohnSnow')
# acc2 = Post('JamieLanister')

# acc1.create_post('good news', 'sansa rodila dochku','http://localhost:8000/images/foto.jpg')
# acc1.create_post('na chile', 'na progulke','htttp://foto.jpg')
# acc1.create_post('egipet','lechu v egiped','http:/foro123.jpg')

# acc2.create_post('Jamie', 'post jamie','http://jamie.jpg')

# print(acc1.user)
# print(acc1.posts)
# print(acc2.user)
# print(acc2.posts)


# print(acc1.retrieve_post(1))
# print(acc1.retrieve_post(5))

# print(acc1.update_post(1,title="suyunchu"))
# print(acc1.retrieve_post(1))
# print(acc1.posts)