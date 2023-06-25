# sentence = input('Vvedite predlojeniye: ')

# if sentence[-1] == '?':
#     print('Voprositel\'noe predlojeniye!')
# else:
#     print('Normal one!')

# vopros = 'Voprositel\'noe predlojeniye!'
# normal = 'Normal one!'
# print(vopros if sentence[-1] == '?' else normal)

# --------------------------------------
# Ternary operator(Тернарный оператор) - это конструкция, которая аналогична по своему действию конструкции if/else, но при этои записывается в одну строчку.

# <выражение если True> if <условное утверждение> else <выражение если False>
from string import digits

# number = input('Vvedite chislo: ')
# # '-5t6'
# for x in number:
#     if x not in digits + '-': #'0123456789-'
#         raise Exception('Вы ввели не число!')
#         # print('Вы ввели не число!')
# number = int(number)
# # 56
# result = number if number >= 0 else -number
# print(result)

# ------------------------------------
import string
flag = True
simbols = string.digits + '-' + '.'
# print(simbols)
# print(type(simbols))
while flag:
    is_correct_nums = True
    num1 = input('Vvedite pervoe chislo: ')
    for x in num1:
        if x not in simbols:
            print('Вы ввели некорректное число!')
            is_correct_nums = False
            break
    if not is_correct_nums:
        continue

    num2 = input('Vvedite vtoroe chislo: ')
    for x in num2:
        if x not in simbols:
            print('Вы ввели некорректное число!')
            is_correct_nums = False
            break
    if not is_correct_nums:
        continue
    
    num1 = float(num1) if '.' in num1 else int(num1)
    num2 = float(num2) if '.' in num2 else int(num2)
    operator = input('Vvedite operator(+, -, *, /): ')
    if operator == '+': print(num1 + num2)
    elif operator == '-': print(num1 - num2)
    elif operator == '*': print(num1 * num2)
    elif operator == '/':
        if num2 == 0:
            print('Нельзя делить на ноль!')
        else:
            print(num1 / num2)
    else:
        print('Неправильный оператор!!')
    
    choice = input('Хотите продолжить(yes/no): ')
    if choice.lower() == 'no':
        flag = False


























