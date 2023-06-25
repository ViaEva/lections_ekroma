# while expression:
#     <body>

# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i}, раз!')
#     i += 1 # i = i + 1 

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' or name2.lower() != 'raychel':
#     name1 = input('vvedite imya1: ')
#     name2 = input('vvedite imya2: ')
#     i += 1
#     if i > 5:
#         print('Цикл остановлен!')
#         break
# else:
#     print('Vy vveli pravilnoe imya!')

# admin = ['John', 'ilovepython123']
# i = 3
# password = None

# while admin[1] != password:
#     password = input(f'{admin[0]} vvedite parol\': ')
#     i -= 1
#     if i == 0:
#         print('Vy zablokirovany na 5 dney!')
#         break
# else:
#     print(f'{admin[0]} vy uspewno zawli v sistemu!')

# --------------------------------------

# for <variable> in <iteravle object>:
#     <body>

# list_ = [0,1,2,3,4,5,6,7,8,9]

# i = iter(list_[::-1])
# print(i)
# print(next(i))
# # print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# for i in list_[::-1]:
#     print(i)

# ----------------------------
# secret_list = ['DeltaViski', 'LOTR123', 'TwentyTwoRiders']
# nick = input('Vvedite svoi nick: ')

# while nick not in secret_list:
#     print('Incorrect nick! Try one more time: ')
#     nick = input('Vvedite svoi nick: ')
# else:
#     print(f'You\'re welcome my dear friend, {nick}!')

# 6 = [3,1,6,2]

# 23436, 190_187_200, 380_457_890_232.

# число 100
# 1, 100
# 2, 4, 5, 10
# 50, 25, 20,

# number1 = 100
# result = [1, number1]

# for i in range(2, int(number1 ** 0.5)+1):
#     if number1 % i == 0:
#         result.extend({i, number1 // i})

# result.sort()
# print(len(result))
# print(result)
# print(number1 ** 0.5)

# ls = []
# for x in result:
#     ls.append(number1/x)
# print(ls)

# set_ = {1,2,3,4,5,6,7,8,9, 9, 9, 9, 9}
# print(set_)
# print(type(set_))
# import random
# ls = []
# for x in range(1, 100):
#     ls.append(random.randint(1,15))

# print(sorted(ls))
# res = list(set(ls))
# print(res)






