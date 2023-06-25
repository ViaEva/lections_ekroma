# # Облвсть видимости и просранства имен или scopes  определякт контекст переменной, в рамках которого мы можем ее использовать

# # built-in (Встроенная) - print, len, max
# # global (Глобальная)
# # enclosed (не локальная, nonlocal)
# # local (локальная область)

# x = 200

# def myfunc():
#     # print(x)
#     x = 300
#     print(x)

# myfunc()
# print(x)


# a = 10 #global
# print # built-in
# def hello(): # global
#     a = 'hello world' # local
#     print(a, 'local inside at func')

# hello()
# print(a, 'global')


# x = 'global'
# print(x, '1')

# def enclosed(): # global
#     x = 'enclosed'
#     def local(): #local
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')


# # LEGB 
# # local - enclosed - global - built in

# len = 5
# # len()
# # print(len([1,2,3,4,5,6,7,8,]))
# a = 10

# def func():
#     # print(a)
#     a = 15
#     print(len)

# func()


# var = 100 # global variable
# x = 5
# def increment():
#     # print(x)
#     # var = var + 1
#     # var += 1 # try to update a global variable inside local scope
#     # print(var)
#     x = 10

# increment()


# # global ->  позволяет имзменять значение глобальной переменнй находясь в локальной области видимости.

# # nonlocal -> позволяет изменять значение не локальной переменнй находясь в локальной области видимости.

# var = 100

# def increment():
#     global var
#     var += 1 # var = var + 1

# print(var)
# increment()
# increment()
# increment()
# increment()
# increment()
# print(var)



def counter():
    num = 0
    def increment():
        nonlocal num
        num += 1
        return num
    return increment

# c = counter()
# print(c) #<function counter.<locals>.increment at 0x7efc766980d0>

# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# print(c()) # 5
# b = counter()
# print(c()) # 6
# print(b()) # 1
# print(c()) # 7

# i = counter()
# for x in range(0, 10000):
#     if x % 3 == 0 and x % 5 == 0:
#         print(i())

# print(i)


# # print(dir(__builtins__))
# # print(len(dir(__builtins__)))

# print(abs(-15)) #Стандартный вызов встроенной функции
# abs = 10 # переопределяем встроенное имя abs
# # print(abs(-15))
# print(abs)
# del abs
# print(abs(-25))
# print(abs)

# print('----------------------\n\n\n')
# print(globals())
# print('--------------\n')
# print(locals())

# -----------------------------

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5], [5,5,5,5]] -> 6, 11, 20 -> 20

# ls = [[100,2,3], [300,3,5], [5,5,5,5], [45,45,6]]
# def find_max(ls):
#     sums = []
#     for x in ls:
#         sums.append(sum(x))
#     return max(sums)

# print(find_max(ls))

# res = max([sum(x) for x in ls])
# print(res)