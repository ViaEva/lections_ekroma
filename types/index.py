# Типы данных в питоне:
# 1. NoneType -> Ничего, пустота
# None #NoneType
# a = None
# print(a)
# 2. Boolean -> Правда или Ложь (True/False)
# True = 1
# False = 0
# 3. Числовые типы данных:
#       а. integer(int) -> Целое число(1,2,3,4,5)
        # b. float() -> Числа с плавающей точкой(1.2, 10.20, 2.7)
        # c. complex() -> комплексные числа(3+5i/j)
# 4. Списковые типы данных:
        # a. list(список/массив) -> [1, 2, 3, True, None]
        # b. tuple(кортеж) -> (1,2,3,False)
        # c. range(последовательность) -> range(1,5) -> 1,2,3,4
# 5. string(str) строка -> "Hello world"
                        #  'Hello world' 

# john = 'My name is John!'
# 6. set() - Множетсво
# 7. dict(Словари) -> содержит данные в виде ключа: значение -> {1: 'one', 2: 'two'}

# **********************************

# Mutable(изменяемые типы данных)
# 1. list()
# 2. set()
# 3. dict()

# Immutable(неизменяемы типы)
# 1. None
# 2. bool
# 3. int(), float(), complex()
# 4. str()
# 5. range()
# 6. tuple()

# ***************************
"""
в пайтоне для вовада данных в терминал используется функция print()
"""
print('Hello world! My name is John Snow!')

# Стандартный ввод данных
'''
Для ввода используется функция input()
'''
a = input('Введите число: ')
print(a)
# type() выводит тип данных
print(type(a))

b = int(input('Введите число номер 2: '))
print(b)
print(type(b))



