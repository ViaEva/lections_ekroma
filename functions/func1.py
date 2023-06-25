# Функции - это именнованая часть программы, которая может вызываться в других частях программы столько раз, сколько угодно

# def name_of_funcion(<a, b> #параметры):
#     <body> # код, какая то логика которая возвращает конечный результат
#     <return> # оператор для возвращения результат

# name_of_function(5, 6 #аргументы)

# Параметры функции - переменные которые будет принимать наша функция, для того чтобы мы могли работать с данными которые передаются в нашу фукнцию

# Аргументы - данные которые мы передаем для параметров при вызове функции

# return - оператор который нужен для того чтобы функция возвращала результат, если return не указать, то возвращает None

# a = print('Hello')
# print(a)

# a = max(range(1,100))
# print(a)


# def our_len(a): # параметр
#     i = 0
#     for x in a:
#         i+=1
#     return i

# ls = [1,2,3,4,5]
# str1 = 'Hello world s vami John Snow!'
# print(our_len(str1)) # аргумент


# def sumTwoNums(num1, num2): # parametrs
#     result = num1 + num2
#     # print(result)
#     return result

# a = sumTwoNums(60, 15) # arguments
# print(a)


# def isEven(num):
#     if num % 2 == 0:
#         return True
#     return False

# a = 10
# b = int(input('Vvedite chislo: '))

# print(isEven(7))
# print(isEven(a))
# print(isEven(b))

# def isEven1(num: int) -> bool:
#     '''Our function returns True or False while checking number for even number'''
#     if num % 2 == 0:
#         return True
#     return False

# print(isEven1(6))
# isEven
# dir


# anna, ded, kabak, kazak, ono, dovod
# from typing import List

# def get_polindrom(words: List[str]) -> List[str]:
#     '''Function return a polndrom string list'''
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result

# some_words = ['John', 'Ono', 'kazak', 'peter', 'anna', 'Dovod', 'apa', 'Juice', 'piko', 'tenet']
# print(get_polindrom(some_words))
# print(get_polindrom(['john', 'jamie', 'from', 'kyrgyzstan']))

'''Напишите функцию которая будет возвращать ваш депозит через определнное время с процентом 10%, возращать финальное количество денег. Мин период вложения 3 года. Мин ставка денек 30 000 сомов'''

# def get_percentage(money: float, period: int) -> float:
#     '''final amount of money'''
#     if money < 30000:
#         raise Exception('Vy vveli nekorektnoe kolichecstvo deneg! min stavka 30 000 somov!')
#     if period < 3:
#         raise Exception('Vy vveli nekorektnyi srok dlya depozita! min srok 3 goda!')
    
#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money = money * 1.1
#         # money + (money / 100 * 10)
#         i += 1
#     return money

# money = float(input('Vvedite summu deneg: '))
# year = int(input('Vvedite srok vashego deposta: '))
# print(get_percentage(money, year))

# ------------------------------

# default params

# def func():
#     print('Hello world!')

# func()

# def print_welcome(name='User'):
#     print(f'Welcome, {name}!')

# print_welcome('John')


# def introduce(name, last_name, work=None):
#     print(f'This persons name is {name}')
#     print(f'This persons last_name is {last_name}')
#     if work:
#         print(f'This persons work is {work}')

# introduce('John', 'Snow', 'King')

# --------------------
# 'Hello world! My name is John, last name is Snow. Nice to meet you!'
# you! meet to Nice Snow. is name....

# hello john snow king
# king snow john hello

# def get_reverse_string(text):
#     print(text[::-1])
#     # print(list(reversed(text)))
#     spisok = text.split()
#     print(spisok[::-1])
#     return ' '.join(spisok[::-1])


# print(get_reverse_string('Hello world! My name is John, last name is Snow. Nice to meet you!'))
# print(get_reverse_string('hello john snow king'))
















