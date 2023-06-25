# """
# 2) Есть глобальная переменная, которая содержит пустой список. Вам необходимо написать функции, одна из которых add() - добавляет в этот список имена, которые вводит пользователь. А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. Вызовите функции в рандомном порядке 10 раз и в конце выведите список.
# """
# import random

# ls = []
# def add():
#     print('ADD!')
#     name = input('Vvedite imya: ')
#     ls.append(name)
#     print(ls)

# def remove():
#     print('REMOVE!')
#     if not ls:
#         print('Увы в списке имен пусо!')
#         return
#     index = int(input('Vvedite index: '))
#     try:
#         print(ls.pop(index))
#     except IndexError:
#         print('Нет такого индекса!')
#     except ValueError:
#         print('Вы ввели некоректный индекс!')
#     print(ls)

# for x in range(0, 10):
#     func = random.choice([add, remove])
#     func()
# print(ls)

# Функция высшего порядка - это функция которая в качестве аргумента принимает другую функцию

# Декоратор - это функция, которая позваоляет без изменения кода обернуть другую функцию для того чтобу расширить функционал обернутой функции

# def decorator(func):
#     print(func)
#     return func()

# def hello():
#     print('Ya hello :)')
#     return 'Hello'

# def john():
#     print('Ya john')
#     return 'John'

# print(hello())
# print()
# print(decorator(hello))
# print()
# print(decorator(john))

# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции {func.__name__}, заняло: {finish-start}')


# def loop():
#     i = 0
#     range_number = 100000
#     while i <= range_number:
#         print(i)
#         i += 1

# benchmark(loop)


# Pythonic way -> @benchmark
#  Синтаксический сахар - Это красота кода

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции {func.__name__}, заняло: {finish-start}')
#     return wrapper

# @benchmark
# def loop():
#     i = 0
#     range_number = 100000
#     while i <= range_number:
#         # print(i)
#         i += 1

# @benchmark
# def add():
#     range_number = 100000
#     ls = []
#     for i in range(0, range_number):
#         ls.append(i)
#     # print(ls)

# loop()
# add()


# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div
# @strong
# @div
# def get():
#     return 'John Snow'

# print(get())


