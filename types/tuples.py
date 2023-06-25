# tuple() - Кортеж, неизменяемый тип данных

# thistuple = ('apple', 'banana', 'cherry')
# print(thistuple)
# print(type(thistuple))

# mytuple = 'apple',
# print(type(mytuple))
# print(mytuple)

# a = [1,2,3,4,5,6,7,8,9]
# b = (1,2,3,4,5,6,7,8,9)
# print('List: ', a.__sizeof__())
# print('Tuple: ', b.__sizeof__())

# tuple_ = tuple('Hello world')
# print(tuple_)

# a = 1
# b = 2
# c = 3
# res = (a, b, c)
# print('Res: ', res)

# new1, new2, new3 = res
# print(new1)
# print(new2)
# print(new3)

# неизмеяемый
# tuple_ = (1,2,3,4,5)
# del tuple_[0]

# print(dir(tuple))

# tuple_ = (1,2,3)
# res = tuple_.index(3)
# print(res)

# tuple_ = (1,2,2,2,2,3,4,5)
# print(tuple_.count(2))


# tuple_ = ('apple', 'banana', 'cherry')
# for x in tuple_:
#     print(x)

# for i in range(0, len(tuple_)):
#     print(tuple_[i])

# i = 0
# while i < len(tuple_):
#     print(tuple_[i])
#     i += 1 # i = i + 1 

# + *
# a = (1,2,3)
# b = (4,5,6)
# print(a + b)
# print(a * 3)

# tuple_ = ('apple', 'banana', 'cherry', 1, 2, 3)
# list_ = list(tuple_)
# list_[0] = 'kiwi'
# tuple_ = tuple(list_)
# print(tuple_)


# a = (1,2,3)
# b = list(a)
# b.append(4)
# a = tuple(b)
# print(a)

# c = (5,)
# a += c # a = a + c
# print(a)



# 1)
# tuple_ = (1,8,3,4,5,8,8,9,2)
# target = 8
# result = (8,3,4,5,8)
# 2)
# tuple_ = (1,2,3,8,5,1,2)
# target = 8
# result = (8,5,1,2)



# tuple_ = (1,2,3,8,5,1,2)
# target = 8

# if tuple_.count(target) > 1:
#     first = tuple_.index(target)
#     second = tuple_.index(target, first + 1) + 1
#     result = tuple_[first:second]
# else:
#     first = tuple_.index(target)
#     result = tuple_[first:]

# print(result)



# Создайте кортеж из 8-ми кортежей учащихся ВУЗов. В кортеже будут присутствовать следующие поля: имя студента, возраст, оценка за семестр, город проживания. Ваш код будет принимать этот кортеж, вычислять среднюю оценку по всем учащимся и выводить на печать следующее сообщение: “Ученики {список имен студентов через запятую} в этом семестре хорошо учатся!”. В список студентов, которые выводятся по результатам работы функции, попадут лишь те, у которых оценка за семестр равна или выше средней по всем учащимся.

# кортеж(имя, возраст, оценка, город)
students = (
    ('Елена', '13', 9, 'Москва'),
    ('Ольга', '11', 7.9, 'Иваново'),
    ('Елизавета', '14', 9.1, 'Тверь'),
    ('Дмитрий', '12', 5.2, 'Челябинск'),
    ('Максим', '15', 6.1, 'Самара'),
    ('Николай', '11', 8.7, 'Владивосток'),
    ('Артур', '13', 5.8, 'Екатеринбург'),
    ('John', '13', 10, 'WinterFell')
)

print(students)
print()
marks = ()
for x in students: 
    marks += (x[2],)

print(marks)


# total_mark = 10
# for student in students:
#     print(student)
#     total_mark += student[2] 
#     # total_mark = total_mark + 10

# avg_mark = round(total_mark / len(students),2)
# print(avg_mark)

# good_students = []
# for student in students:
#     print(student)
#     if student[2] > avg_mark:
#         good_students.append(student[0])
# print(good_students)

# print(f'Ученики {", ".join(good_students)} в этом семестре хорошо учатся!')








