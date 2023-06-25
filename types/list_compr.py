# list comprehensions - генераторы списков

# list comprehensions - упрощенный подход к созданию списков, который задействует цикл for, а также конструкции if else для определения того, что в итоге окажется добавлено в наш список

# list -> 0: 200 -> num % 2 = 0

# ls = []
# for x in range(0,200):
#     if x % 2 == 0:
#         ls.append(x)
# print(ls)

# ls = [x for x in range(0, 200) if x % 2 == 0]
# print(ls) 

# list -> 0-300: x%2=0 and x%3=0

# ls = []
# for x in range(0, 300):
#     if x % 2 == 0 and x % 3 == 0:
#         ls.append(x)
# print(ls)

# ls = [x for x in range(0, 300) if x % 2 == 0 and x % 3 == 0]
# print(ls)

# list: 0-100 -> x%2=0: x**2 else x

# ls = []
# for x in range(0, 100):
#     if x % 2 == 0:
#         ls.append(x ** 2)
#     else:
#         ls.append(x)
# print(ls)

# ls = [x**2 if x % 2 == 0 else x for x in range(0, 100)]
# print(ls)

# ---------------------------------------

# newlist = [expression for item in iterable <if condition == True>]

# ls = []
# for i in range(0, 100, 2):
#     ls.append(i)
# print(ls)

# ls = [i for i in range(0, 100, 2)]
# print(ls)

# ls = [i**2 for i in range(0, 11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon']

# ls = [x.capitalize() for x in fruits]
# print(ls)

# ls = [x for x in fruits if 1]
# print(ls)

# ls = [x.upper() for x in fruits if x != 'apple']
# print(ls)


# ls = [[1,2,3], [4,5,6], [7,8,9]]
# result = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# result = []
# for inner_list in ls:
#     # print(inner_list)
#     for x in inner_list:
#         result.append(x)
# print(result)

# result = []
# for x in ls:
#     result.extend(x)
# print(result)

# result = []
# for x in ls:
#     result += [*x]

# print(result)


# ls = [[1,2,3], [4,5,6], [7,8,9]]
# result = [x for inner in ls for x in inner]
# print(result)

# -----------------------------------------

# from datetime import datetime

# start = datetime.now()
# # ls = [x for x in range(0, 10_000_000)]
# # ls = []
# # for x in range(0, 10_000_000):
# #     ls.append(x)
# finish = datetime.now()
# print(finish-start)


# ls = [x + 10 if x == 8 else x + 100 for x in range(0, 10)]
# print(ls)

# ---------------------------------
# dict comprehensions

# dict_ = {
#     'key1': 'value1',
#     'key2': 'value2'
# }

# dict_ = {x: x**2 for x in range(1, 15)}
# print(dict_)


# dict1 = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4,
#     'e': 5, 'f': 6, 'g': 7, 'h': 8
# }
# # 'a': 'odd', 'b': 'even'

# 1: {1: 2}
# new_dict = {k: ('even' if v % 2 == 0 else 'odd') for k, v in dict1.items() for value in v.values()}
# print(new_dict)

# names = ['John', 'Tirion', 'Jamie', 'Sansa', 'Harry']

# dict_names = {i: value for i, value in enumerate(names)}
# print(dict_names)

# for i, value in enumerate(names):
#     print(i, value)


# a = ['John', 2, 3, 4, 'hello', 5]
# b =[]


# for i, v in enumerate(a):
#     if i == a.index('hello'):
#         print(i, v)
    # b.append(i)
    # b.append(v)

# print(b)


# ---------------------------------

# dict_ = {
#     'Timur': {'history': 90, 'math': 101, 'literature': 100}, 
#     'Olga': {'history': 100, 'math': 96, 'literature': 81}, 
#     'Nik': {'history': 105, 'math': 85, 'literature': 87}
# }
# new_dict = {inner_key: x for inner_key, inner_value in dict_.items() for x in inner_value if max(inner_value.values()) == inner_value[x]}
# print(new_dict)


# new_dict = {}
# for key, value in dict_.items():
#     # print(value)
#     # print(max(value.values()))
#     for x in value:
#         # print(value[x])
#         if value[x] == max(value.values()):
#             new_dict.update({key: x})

# print(new_dict)


# dict_ = {
#     'Timur': {'history': 90, 'math': 101, 'literature': 100}, 
#     'Olga': {'history': 100, 'math': 96, 'literature': 81}, 
#     'Nik': {'history': 105, 'math': 85, 'literature': 87}
# }
# new_dict = {k: max(v, key=v.get) for k, v in dict_.items()}
# print(new_dict)


# 2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
# Например: 
# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# Результат:
# {'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}

# a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
# print(a)
# dict_ = {key: {k: v+2 for k, v in value.items()} for key, value in a.items()}
# print(dict_)

