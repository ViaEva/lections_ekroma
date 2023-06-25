# dict() - Словарь -> упорядоченная коллекция элементов (python 3.7 -> ordered). Каждый элемент в словаря содержится в паре ключ: значение.

# Ключи должны быть уникальными и быть неизменяемым типом данных(str, int, tuple etc.). Тогда как значениями могут выступать любые типы данных.

# thisdict = {
#     'brand': 'Ford',
#     'model': 'Mustang',
#     'year': 1964
# }

# print(thisdict)
# print(type(thisdict))

# ассоциативный массив, hash tables, object(js), structure == dictionary(py)

# a = {1, 2, 3} #set
# tuple_ = 1, 2, 3 #tuple
# print(type(a))
# print(type(tuple_))

# a = dict()
# print(type(a))

# dict_ = dict([('key1', 'value1'), ('key2', 'value2')])
# print(dict_)
# print(type(dict_))

# dict( ( (key, value)  (key, value) ) )
#     {  'key1':'value1', 'key2': 'value2'  }

# ------------------------------------

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',
    # [1,2,3]: 'list' #error
    # 'first_name': 'Raychel'
# }
# print(user_info)
# print(user_info.get('age1'))
# print(user_info['role1'])
# -------------------

# print(dir({}))

# items, keys, values

# user_info = {
#     'first_name': 'John',
#     'last_name': 'Snow',
#     'age': 24,
#     'email': 'johnsnow24@gmail.com',
#     'role': 'moderator',}

# print(user_info.values())
# print(user_info.keys())
# print(user_info.items())

# for value in user_info.values():
#     print(value)

# for k, v in user_info.items():
#     print('Key', k)
#     print('Value', v)
#     print()

# a = dict([(1, 2), ('1', '2')])
# print(a)
# b = {1: 2, "1": '2'}
# print(b.items())

# for x in b.items():
#     print(x)
#     print(type(x))

# изменение элементов в словаре

# dict_ = {'name': "Jack", 'age': 24}

# dict_['name'] = 'John'
# dict_['adress'] = 'Toktogula str.'
# print(dict_)


# dict_ = {'name': "Jack", 'age': 24}

# dict_.update({'name': 'John', 'adress': 'Kiev str.'})
# print(dict_)



# dict_ = {}
# list_ = list(range(1, 200))

# new_dict = dict_.fromkeys(list_, 'value')
# print(new_dict)


# setdefault - работает примерно так же как и метод get(), но если такого ключа нет то он создаст новую пару.

# dict_ = {'name': "Jack", 'age': 24}

# print(dict_.setdefault('age'))

# dict_.setdefault('address', 'Moskow str.')

# print(dict_)

# Удаление элементов

# pop(key) - удаляет по ключу

# dict_ = {'name': "Jack", 'age': 24}
# removed = dict_.pop('age')
# print(dict_)
# print(removed)

# removed = dict_.pop('address', 'No such key!')
# print(dict_)
# print(removed)


# popitem() - Удаляет последнюю пару

# dict_ = {'age': 24, 'name': "Jack"}
# dict_['address'] = 'Kiev str.'

# removed = dict_.popitem() 
# print(dict_)
# print(removed)

# ----------------------------------------

# roles = {
#     0: 'Moderator',
#     1: 'Admin',
#     2: 'Customer',
#     3: 'Vendor'
# }

# users = [
#     {
#         'id': 1,
#         'username': 'John',
#         'role': roles[1]
#     },
#     {
#         'id': '2',
#         'username': 'Raychel',
#         'role': roles[3]
#     }
# ]

# product = {
#     'id': 1,
#     'title': 'Iphone 14',
#     'description': 'Lorem ipsum',
#     'price': 200
# }

# print(product)
# id_user = int(input('Vvedite vaw id: ')) - 1

# print(users[id_user])
# if users[id_user]['role'] == roles[1]:
#     choice = input('Vvedite chto izmenit\': ')
#     new = input('Vvedite new value: ')
#     product.update({choice: new})
# else:
#     raise Exception('Permission denied!!')

# print(product)
# imya function
#     ls = []
#     for x in rnage
#         appendx

# comp

# list(function)


