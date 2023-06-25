# JavaScript object Notation - JSOND Единый формат хронения и  передачи данных между компютерами, сервисами, приложениями и программами через инет
# <filensme>.JSON

# {
#     "id":1,
#     "id":2,
#     "id":3
# JSON object == {}. PY dict == {}. JSON == {}

# Процессы сериализации и десериализации данных

# Сериализация(Запись данных в JSON) - это перевод Python Dict В JSON Формат

# dumb - метод записывает объект Python в фацл в формате JSON
# 

#  Десереализация(Чтение данных из JSON) - Это процесс перевода из JSON в PYTHON Dict

#  load - метод который считывает файл в формате JSON и переводит ето в объекты Python 
# loads - метод который считывает текст в формате JSON и переводит его в объект

# -----------------------------------------

import json
from urllib.request import urlopen

data = urlopen('https://randomuser.me/api/')
print(type(data))
print(data)

