# Встроенные функции

# input()
# print()
# str() etc.

# map()
# filter()
# lambda
# enumerate()


# Анонимные функции - lambda(такие же функции только без названия)
# lambda функции могут приниматьсколько угодно аргументов, но всегда возвращают только одно
# выражение

# def sum_args(a, b):
#     res = a + b
#     return res

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_args2 = lambda a, b: a + b
# # x = int(input())
# print(sum_args2(5, 7))

# x = lambda a, b, c: (a * b) % c
# print(x(5, 7, 10))

# get_keys = lambda x: x.keys()
# dict_ = {1: '1', 2: '2', 3: '3', 4: '4', 5: 'Hello'}
# print(get_keys(dict_))

# get_last = lambda ls: ls[-1]
# ls = [1,2,3,4,5,6,7,8,9,'Hello',6]
# print(get_last(ls))


# def myFunc(n):
#     return lambda a: a * n

# myDoubler = myFunc(2)
# myTripler = myFunc(3)
# multiOneHundred = myFunc(100)

# print(myDoubler(50))
# print(myDoubler(22))
# print(myTripler(11))
# print(myTripler(22))
# print(multiOneHundred(3))


# dict_ = {'Sanzhar': 50000, 'John': 170000,
# 'Ayana': 1000000, 'Sultan': 10}

# print(dict_.items())
# new_dict = sorted(dict_.items(), key=lambda x: x[1], reverse=True)

# print(dict(new_dict))
# ls = ['Str', 'Ayana', 'ayana', 'Sultan', 'sultan', 'John', 5]
# print(sorted(ls, key=len))

# ---------------------------------------

# map(function, Iterable) - применяет функцию к каждому элементу из последовательности и возращает mapobject(итератор) с результатом.

# Например, с помощью map, можно преобразовать элементы. Перевести все строки в верхний регистр

# ls = ['one', 'two', 'three', 'dict',]
# result = list(map(str.upper, ls))
# print(result)
# result1 = list(map(len, ls))
# print(result1)

# names = ['John', 'Sultan', 'Ayana', 'Tirion']
# # ['Hello mr/mrs John', 'Hello mr/mrs Ayana', ...]

# result = list(map(lambda x: f'Hello mr/mrs {x}', names))
# print(result)

# dict_ = {1: 2, 3: 4, 5: 6}
        # {1: '2', 3: '4', 5: '6'}
# print(dict_.items())

# result = dict(map(lambda x: (x[0], str(x[1])), dict_.items()))
# print(result)

# -----------------------------------------

# from random import choices
# from string import ascii_letters, digits, punctuation
# from itertools import repeat

# symbols = '_()+-!@#%'
# q_pass = int(input('vvedite kolichestvo paroley: '))

# result = {
#     f(choices(ascii_letters, k=10), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x+y+z)), q_pass)
# }
# print(result)
# print(f'Quantity of passwords: {len(result)}')

# from statistics import mean

# dlina = [len(x) for x in result]
# print(f'Средняя длина пароля: {mean(dlina)}')

# ------------------------------------
# filter(function, Iterable) -> применяет ко всем элементам iterable функцию которую мы передали и возращает итератор с теми объектами,для которых функция вернула True

# ls = ['one', 'two', 'list', '', '100', '1', '50', 'john99']

# res = list(filter(str.isdigit, ls))
# print(res)


# ls = [10, 11, 102, 213, 314, 515,]
# res = list(filter(lambda x: x % 2 != 0, ls))
# print(res)


# def func(stroka):
#     if len(stroka) >= 4:
#         return True
#     return False

# x = lambda stroka: len(stroka) >= 4

# ls = ['John', 'one', 'two', 'list', 'makers', 'py.22', 'ono']
# res = list(filter(func, ls))
# res1 = list(filter(x, ls))
# print(res, res1)

# ---------------------------------
# enumerate(iterable)

# ls = ['str1', 'str2', 'str3']

# x = list(enumerate(ls))
# print(x)

# for i, x in enumerate(ls):
#     print(f'Index {i}, Element {x}')


# ---------------------------------

# zip(iterables) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает его

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = list(zip(ls1, ls2))
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 400, 500]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)

# zip для создания словарей
# x = [(1, 2)]
# a = dict(x)
# print(a)

# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['castle_r1', 'winter_fell', 'Starks', 'Cisco', '16.0', '10.255.0.1']

# res = dict(zip(d_keys, d_values))
# print(res)


# d_keys = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# data = {
#     'r1': ['london_r1', '21 New Globe Walk', 'Cisco', '4451', '15.4', '10.255.0.1'],
#     'r2': ['london_r2', '21 New Globe Walk', 'Cisco', '4451', '15.4', '101.25.10.2'],
#     'sw1': ['london_sw1', '21 New Globe Walk', 'Cisco', '3850', '16.0', '55.251.0.101']
# }

# london_data = {}
# for k in data:
#     london_data[k] = dict(zip(d_keys, data[k]))

# print(london_data)

# -------------------------------
# all(), any()

# all(Iterable) - Возвращает True, если все элементы внутри объекта инсттина, иначе False

# [1,2] - True
# [] - False
# 5 - True
# 0 - False
# -1 - True
# 's' - True

# ls = [[1,2], 5, 'stroka', True, 1, '']
# print(all(ls))

# ip = '10.255.0y.202'

# result = all(i.isdigit() for i in ip.split('.'))
# print(result)

# any - Возвращает True, если хотябы один элемент истинна

# ls = [0, 0, '', False, '123']
# print(any(ls))


# def ignore_command(command):
#     ignore = ['rm -rf', 'alias', 'reset']
#     for word in ignore:
#         if word in command:
#             return True
#     return False

# command = input('Vvedite commandu: ')
# if ignore_command(command):
#     raise Exception('Invalid command')
# print('Vse ok!')


# ignore = ['rm -rf', 'alias', 'reset']
# command = input('Vvedite commandu: ')

# if any(word in command for word in ignore):
#     raise Exception('Invalid command!')
# print('Vse ok!')

# ---------------------------

# ls = [2, '2', 3, '4', '6', 45, '16', 5, '1']

# res = [x**2 for x in filter(lambda x: type(x) == int, ls)]
# res1 = [x**2 for x in ls if type(x)==int]
# print(res)
# print(res1)

# -----------------------------

# def func(x, b, a):
#         print(x)
#         print(b)
#         print(a)

# func(a=1, x=2, b=3)

# def func(name, last_name, age, *args, **kwargs):
#     print('Имя:', name)
#     print('Фаимилия:', last_name)
#     print('Возраст:', age)
#     if args:
#         print('Cтатус:', args[0])
#         print('Cупруг:', kwargs)
#     else:
#         print('Cтатус: Холост(-а)')

# func('John', 'Snow', 26)
# func('Tirion', 'Lanister', 21, 'Женат', wife_name='Sansa', wife_last_name='Stark')

