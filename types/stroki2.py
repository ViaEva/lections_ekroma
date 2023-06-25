# print(dir(str))


# replace(old, new, [count]) - Меняет в строке old на new значение, если вы укажете count, то он заменит count раз.

# text = 'ha ha ha ha'
# # print(text[::-1])
# result = text.replace('a', 'i', 2)
# print(result)
# # print(text)
# str1 = 'Hello world! My name is John Snow!'
# # print(str1.replace('name', 'nama', 1))
# result = str1[0:12] + str1[12:].replace('e', 'a')
# print(result)

# strip() - Убирает пробельные символы в начале и в конце строки.
# rstrip, lstrip

# text = input('Enter the text: ')
# print(text)
# result = text.strip()
# print(result)

# text = '   Hello   '
# print(len(text))
# result = text.rstrip()
# print(result)
# print(len(result))


# startswith(string, [start], [end]) - Возвращает True если строка начинается с string, иначе False
# text = 'Hello world'
# print(text.startswith('W'))
# print(text.startswith('H'))
# print(text.startswith('Hello'))
# print(text.startswith('d', -1))
# print(text.startswith('wo', 6))
# print(text.startswith('h'))

# -------------------------
# print(id('h'))
# print(id('H'))
# -------------------------

# print(dir(str))

# isalpha() - проверяет состоит ли наша строка из символов(букв латинского алфавита или киррилицы)
# isdigit() - проверяет состоит ли наша строка полность из чисел True
# isnumeric() - проверяет состоит ли наша строка полностью из чисел

# text = 'Привет57'
# print(text)
# print(text.isalnum())
# text.isnumeric


# 'hello'

# text = 'df5f'
# print(text.isdigit())
# print(text.isnumeric())

# isdigit()
# islower()
# isupper()
# istitle()
# isalpha()

# str.istitle()

# index(value, [start], [end]) - выводит индекс значения value в нашей строке

# text = 'Hello world! My name is John!'
# result = text.index('o', 24)
# print(result)

# rindex - поиск с конца

# find(value, [start], [end]]) - делает тоже самое что и метод index. Разница в том что, если value не найден, то возращается -1
# rfind

# text = 'Hello'
# print(text.rfind('l'))


# count('string', [start]) - считает количесво вхождений string  внашу строку

# text = 'Hello world! I\'m from Earth!'
# result = text.count('Hello')
# print(text.count('e'), text.count('o'))

# swapcase() - Возвращает строку, в которой каждая буква будет иметь противоположный регистр
# upper(), lower()
# text = 'Hello World, JohN, SNOW'
# print(text.swapcase())
# print(text.lower())
# print(text.upper())

# capitalize() - переводит первую букву в верхний регистр

# print('hello'.capitalize())
# print(input('Vvedite vashe imya: ').capitalize().istitle())

# title() - переволит символы всех слов в строке в верхний регистр
# text = 'john jamie sansa nursultan jerry'
# print(text.title())
# print(text.capitalize())

# split(разделитель) - Дробит строку по разделителю который находится в строке. Разделяет строку и возвращает тип данных list
# text = 'Let me speak from my hearth in English! My name is John!'
# ls = text.split(' ')
# print(len(ls))

# разделитель.join(iterable) - соединяет строки, которые находятся в iterable по  разделителю

# sentence = ' '.join(ls)
# print(sentence)
# sentence = ' | '.join(ls)
# print(sentence)

'Hello' # 'oellH'
'sentence' # eentencs

word = 'John'
result = word[-1] + word[1:-1] + word[0]
print(result)

word = 'sentence'
result = f'{word[-1:]}{word[1:-1]}{word[:1]}'
print(result)

