# def sum_of_args(a, b, c, d): #a,b,c,d параметры
#     return a + b + c + d

# result = sum_of_args(1,2,3,4)
# print(result)
# print(type(result))
# print(result(5, 10, 15, 20))

# ls = [1,2,3,4,5]
# print(ls.append(16))

# -----------------------------------------
# Позиционные и именованные аргументы

# def printParams(a=None, b=None, c=None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')

# printParams(a=1, b=2)


# def sum_of_args(a, b, c, d): #параметры
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # arguments(Позиционные аргументы)
# print(sum_of_args(a=5, c=20, d=15, b=10)) # keyword arguments(Именованные аргументы)
# print(sum_of_args(10, 50, d=50, c=100))

# -------------------------------------
# оператор *

# a = [1,2,3]
# b = [4,5,6]
# c = [*a, *b]
# print(c)

# ----------------------------------
# *args, **kwargs в фунциях

# def printScores(student, *scores):
#     print(f'Student name: {student}')
#     # print(scores)
#     # print(type(scores))
#     for x in scores:
#         print('Score:', x)

# printScores('John', 100, 90, 95, 88, 96)

# def print_pet_names(owner, **pets):
#     print(f'Owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) is list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# print_pet_names('John Snow', dog='Rex', cat='Larry', fish=['Nemo', 'Dori', 'Alex'], turtle='Leonardo')


# def get_some_data(a, b, *args, **kwargs):
#     print('параметры а и b:', a, b)
#     print('Аргументы:', args)
#     print('Именованные аргументы:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1,2,3,4,5, lang='Pyhton', name='John Snow', car='BMW M8')

# ---------------------------------

# def generate_random_string(len_):
#     import string as s
#     import random
#     random_str = ''.join(
#         random.choice(s.ascii_lowercase + s.ascii_uppercase + s.digits) for i in range(0, len_)
#         )
#     return random_str

# print(generate_random_string(50))

# -----------------------------------

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'

def calc(num1, num2):
    operator = input('Введите оператор(+,-,/,*): ')
    if operator == '+': return add(num1, num2)
    elif operator == '-': return subtract(num1, num2)
    elif operator == '*': return multiply(num1, num2)
    elif operator == '/': return divide(num1, num2)
    else: return 'Вы ввели неверный оператор!'

def main():
    try:
        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Вы ввели некоректное число!')
        main()
        return

    while True:
        result = calc(num1, num2)
        if type(result) != float:
            print(f'Result: {result}')
        else:
            print(f'Result: {result}')
            break

    question = input('Хотите продолжить?(Yes): ')
    if question.lower() == 'yes':
        main()
    else:
        print('Спасибо за использование нашего калькулятора! Пока!')

main()















