# Операторы сравнения
# Условные операторы
# # Логические операторы +
# is in not +

# Операторы сравнения
# <, >, ==(равно), <=, >=, !=(не равно)

# num1 = 18
# num2 = 15
# print(18 < 15)
# print(type(5))
# stroka1 = 'Hello!'
# stroka2 = 'World'
# print(stroka1 < stroka2)
# print(ord('H'))
# print(ord('W'))
# print(len(stroka1) > len(stroka2))

# text = 'Hello world! My name is John!'
# for letter in text:
#     print(ord(letter))

# print(chr(1080))


# Условные операторы
# if
# elif
# else

# if <condition>:
#     <body if>
#     <body if> #сработает если в if придет True
# elif <condition>:
#     <body elif>
# elif <condition>:
#     <body elif>
# else:
#     <body> #сработает если во всех условиях пришло False

# string = input('Enter smt: ')

# if string == 'Hello':
#     print('Hello stranger!')
# elif string == 'John':
#     print('Welcome back John Snow!')
# elif string == 'Mercedez':
#     print('Mercedez-Benz S class!')
# else:
#     print('Совпадений не найдено!')

# print('Код закончился!')


# email = input('Enter email: ')
# password1 = input('Enter password: ')

# if len(password1) < 8:
#     raise Exception('Too short password!')

# password2 = input('Enter password confirmation: ')

# if password1 != password2:
#     raise Exception('Password didn\'t match!')
# else:
#     print('Successfully signed Up!')


# age = input('Enter your age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError('Enter correct values!!')

# if age < 18:
#     print(f'Chuvak prihodi cherez {18 - age} goda/let!!!')
# else:
#     print('Vy prohodite po vozrastu!')
# import string

# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)


# password = input('Enter your password: ')
# symbols = ['_', ',', '.', '%', '#', '@', '+', '-', '*', '(', ')']
# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# flag = False
# for element in symbols:
#     if element in password:
#         flag = True

# flag_nums = False
# for num in nums:
#     # print(num)
#     if num in password:
#         flag_nums = True

# if not flag_nums:
#     raise Exception('Вы ввели только буквы b символы, нужны еще цифры!')
# elif password.isdigit():
#     raise Exception('Вы ввели только цифры, нужны еще буквы!')
# elif not flag:
#     raise Exception('Вы не ввели хотя-бы один спец-символ в пароль!!(_,.()*...)')
# else:
#     print('Все окей вы ввели корректный пароль!')

# Логические операторы
# and -> Логическое и
# or -> лог или
# not -> лог отрицание

# Операторы идентификации
# in -> проверяет наличие элемента внутри какого либо массива или строки
# is -> сравнивает ячейки памяти двуъ элементу
    # == -> сравнивает по значение
# is not -> отрицательное сравнение ячеек памяти

# my_age = 20
# your_age = 18
# result = my_age == 21 and your_age == 18
# print(result)

# result = my_age < 18 or your_age < 17
# print(result)

# result = not my_age > 25
# print(result)


# is_google_user = True
# is_github_user = False
# is_age_greater_21 = False
# user_coins = 8000

# if (is_google_user and is_github_user) and (is_age_greater_21 or user_coins > 5000):
#     print('You can enter the system mr John Snow!')
# else:
#     print('Sorry, you couldn\'t enter!')


# str1 = 'Hello world!'
# choice = input('Vvedite simvol: ')

# if choice in str1:
#     print(f'Символ {choice} есть в строке: "{str1}"')
# else:
#     print(f'Символа {choice} нет в строке: "{str1}"')


# dano [1--100]
# \3 -> <3> - fu
# \5 -> <5> - ba
# \3, \5 -> <15> - fuba

# for number in range(1,100):
#     if number % 3 == 0 and number % 5 == 0:
#         print(f'{number} - fuba')
#     elif number % 5 == 0:
#         print(f'{number} - ba')
#     elif number % 3 == 0:
#         print(f'{number} - fu')

# print('sad')

# num = 1
# while num >= 0:
#     num = int(input('Vvedite chislo: '))
#     if num < 0:
#         print('Встретилось отрицательное число')




