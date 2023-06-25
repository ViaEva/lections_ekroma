# set() - Множеств в python - "Контейнер", который содержит в себе уникальные элементы в неупорядоченном виде.

# # {} !!!!!!
# a = {} -> множество {1,2,3,4,5,6,7}
# d = {1: 'a', 2: 'b'} -> словари


# set_ = {1,2,3,4,5,6,7,7,7,7,}
# print(set_)

# ls = [1, 2, 'a', False, 3, 4, 5, 6, 7]
# str1 = 'Hello world!'
# ls.extend(str1)
# print(ls)

# set_ = {*ls}
# print(set_)
# print(type(set_))

# ls = [1,2,3,4,5]

# print(ls)
# print(*ls)
# print(1,2,3,4,5)

# tuple() set(), 

# {*ls} == {1,2,3,4,5}

# a = {1,2,3,4,5}
# print(a)
# print(type(a))
# # print(dir(a))
# a.pop()
# print(a)


# Составьте код которая принимает номер месяца вашего рождения и в зависимости от сезона печатает на выходе следующее:
# «Вы родились в <НАЗВАНИЕ_МЕСЯЦА>. <ОПИСАНИЕ_СОБЫТИЙ>».

# В качестве ОПИСАНИЯ_СОБЫТИЙ будет характеристика сезона: 
# - для зимы «За окном падал белый снег»,
# - для весны «Птицы пели прекрасные песни»,
# - для лета «Солнце светило ярче чем когда-либо»,
# - для осени «Урожай был невероятным».

# Важно учесть, что пользователи могут ввести любой тип данных в качестве аргумента (не попадитесь на этом и предупредите о том, что «Требуется ввести реальный номер месяца»).

# months = {
#     1: 'Январе',
#     2: 'Феврале',
#     3: 'Марте',
#     4: 'Апреле',
#     5: 'Мае',
#     6: 'Июне',
#     7: 'Июле',
#     8: 'Августе',
#     9: 'Сентябре',
#     10: 'Октябре',
#     11: 'Ноябре',
#     12: 'Декабре'
# }

# while True:
#     number = input('Введите номер месяца: ')
#     if number == 'john':
#         break

#     if not number.isdigit():
#         print('Требуется ввести реальный номер месяца')
#         continue
#     number = int(number)
#     if number not in range(1, 13):
#         print('Требуется ввести реальный номер месяца')
#         continue
    
#     if number in range(3, 6):
#         print(f'Вы родились в {months[number]}. Птицы пели прекрасные песни.')
#     elif number in range(6, 9):
#         print(f'Вы родились в {months[number]}. Солнце светило ярче чем когда-либо.')
#     elif number in range(9, 12):
#         print(f'Вы родились в {months[number]}. Урожай был невероятным.')
#     else:
#         print(f'Вы родились в {months[number]}. За окном падал белый снег.')


# --------------------------------

# Counting Valleys Haccerrank
# https://www.hackerrank.com/challenges/counting-valleys/problem


# Input1:
# path = 8
# way = 'UDDDUDUU'
# Output:
# 1
# Input2:
# path = 12
# way = 'DDUUDDUDUUUD'
# Output:
# 2
# Input3:
# path = 10
# way = 'UDUUUDUDDD'
# Output:
# 0


path = 8
way = 'UDUUUDUDDD'

sea_level = 0
dolina = 0
for step in way:
    if step == 'U':
        sea_level += 1 
        # sea_level = sea_level + 1
        if sea_level == 0:
            dolina += 1
    elif step == 'D':
        sea_level -= 1

print('долин пройдено:', dolina)




