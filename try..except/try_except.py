# Обработка исключений
# Operator: try...except


# Ошибки -> связаны с кодом:
# Syntax Error
# IndentationError
# TabError

# Исключения -> Invalid values
# ZeroDivisionError
# ArithmeticError
# NameError
# KeyError
# ValueError
# ImportError
# BaseException #Прородитель всех ошибок

# try...except

# try:
#     <expression>
# except <Exception>:
#     <body>
# <else>: Если все окей
#     <body>
# <finally>: В любом случае в конце
#     <body>

# print(dir(__builtins__))

# num1 = int(input('Vvdite chislo: '))
# print(num1)
# print('Ochen\' vajnaya strochka koda!')

# try:
#     num1 = int(input('Vvdite chislo: '))
#     print(num1)
# except:
#     print('Invalid Value, try again!')

# print('Ochen\' vajnaya strochka koda!')

# Способы увидеть ошибку
# 1. import sys
# ls = [1,2,3,4,5]
# try:
#     index = int(input('Vvedite index: '))
#     print(ls[index])
# except:
#     import sys
#     print(f'oops, we catched {sys.exc_info()[0]} error!')

# 2. Exception as e
# ls = [1,2,3,4,5]
# while True:
#     try:
#         index = int(input('Vvedite index: '))
#         print(ls[index])
#     except Exception as e:
#         print(f'oops, we catched {e.__class__} error!')


# try:
#     num1 = int(input('Vvedite chislo 1: '))
#     num2 = int(input('Vvedite chislo 2: '))
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Vy vveli nekorektnye dannye!')


# try:
#     num1 = int(input('Vvedite chislo 1: '))
#     num2 = int(input('Vvedite chislo 2: '))
#     result = num1 / num2
# except ValueError:
#     print('Vy vveli nekorektnye dannye!')
# except ZeroDivisionError:
#     print('Na nol\' delit\' nel\'zya!')
# else:
#     print('Result of division', result)
# finally:
#     print('The end')










