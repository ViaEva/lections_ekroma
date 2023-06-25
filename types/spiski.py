# list()(список, массив) - изменяемый, последовательный тип данных, который из себя представляет коллекцию каких либо объектов(значений).

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# print(my_list[0])
# print(my_list[-1][0:2])

# list()
# my_list = list('Hello world!')
# print(my_list)
# print(len(my_list))

# tuple_ = ('banana', 'apple', 'cherry')
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))


# range() - возвращает последовательность элементов(числа)

# ls = list(range(1, 100, 2))
# print(ls)

# ls = list(range(0, 101))
# print(ls)

# for x in ls:
#     # print(x)
#     if x % 2 == 0:
#         print(f'Число {x} четное, квадрат {x**2}')
#     else:
#         print(f'Число {x} нечетное, куб {x**3}')

# print(dir([]))

# append(element) - Добавляет element в конец списка

# list_ = [1,2,3]
# print(list_)
# list_.append(5)
# list_.append([1,2,3])
# print(list_)
# print(a)

# extend(element[iterable]) -> расширяет спписок добавляя element в конец.

# ls = [1,2,3]
# ls.extend('Hello')
# ls.append((11, 12, 13))
# print(ls)

# insert(<index>, <element>) -> Добавляет element по указнному index

# ls = ['string', 2, 3, False]
# ls.insert(1, 1)
# ls.insert(-1, None)
# print(ls)

# index(element, [start], [end]) -> возвращает индекс elementa в списке

# ls = ['Hello', 'world', 'my', 'name', 'is', 'John', 'North', 'king', 'queen', 'USA']
# str1 = input('Vvedite slovo: ')

# if str1 in ls:
#     print(f'"{str1}" is in list: {ls.index(str1)}')
# else:
#     print('Isn\'t')

# id = ls.index('USA')
# print(id)
# print(ls[ls.index('USA')])
# print(ls[8])

# count(element) -> Возвращает кол-во вхождений element в списке

# ls = [1,2,3,4,5,6,7,8,9,5,5,5]
# result = ls.count(5)
# print(result)

# remove(element) -> удаляет element, но если такого элемента нет в списке, то тогда выводится ошибка
# pop([index]) -> удаляет и возращает элемент по index, но если index не указан, то удаляет последний элемент.

ls = [5,1,2,3,4,2,3,5]

# for x in ls:
#     if 5 in ls:
#         ls.remove(5)

# print(ls)

# ls.pop(5)
# for x in ls:
#     if 5 in ls:
#         ls.pop(ls.index(5))
# print(ls)
# deleted = ls.pop()
# print(ls)
# print(deleted)

# sort() - сортирует список, если в аргументах передать reverse=True, то список будет отсортирован в убывающем порядке
# import random

# ls = []
# for x in range(0, 200):
#     ls.append(random.randint(0, 1000))

# ls.sort(reverse=True)
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'apple', 'SultanJasha', 'Ayana']

# print(ls)
# ls.sort(key=len, reverse=True)
# print(ls)

# for x in ls:
#     print(ord(x[0]))

# ls = [1, 'h', 3]
# ls[1] = 2
# ls[2] = 4
# print(ls)

# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)

# print(spisok)

#  Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#1) nums = [2,7,11,15]
# target = 9
# # 0, 1  -------- 2 + 7 = 9
#                  9 - 2 = 7
#                  9 - 7 = 2

#2) nums = [4,11,2,5,1,6]
# target = 8
# # 2 5

# nums = [4,11,2,5,1,6]
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num == nums[i]:
#             continue
#         k = nums.index(num)
#         print(f'Otvet: {i} {k}')
#         break






