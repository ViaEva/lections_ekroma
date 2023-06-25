import json

FILE = 'jsondb/users.json'

class RegisterMixin:
    'Миксин для регистрации юзера'
    def validate_password(self, password, password2):
        if len(password) < 8: raise ValueError('Пароль слишком короткий!')
        elif password.isdigit() or password.isalpha(): 
            raise ValueError('Пароль должен состоять из чисел и из букв!')
        elif password != password2: raise ValueError('Пароли не совпали!')
    def registr(self, username, password, password2): 
        self.validate_password(password, password2)

        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1
            except (IndexError, ValueError):
                id = 1
                data = []
        with open(FILE, 'w') as file:
            if data:
                is_username_used = any([x['username'] == username for x in data])
                if is_username_used:
                    json.dump(data, file)
                    raise ValueError('Такой username уже существует!')
            data.append({'id': id, 'username': username,'password': password,}) 
            json.dump(data, file)
            return {'status': 201, 'msg': 'Successfully registrated!'}

class LoginMixin:
    'Миксины для логина'
    def login(self, username, password):
        with open(FILE, 'r') as file:
            data = json.load(file)
            is_registrated = any([x['username'] == username for x in data])
            if not is_registrated:
                raise Exception('Нет такого юзера')
            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            if user_data['password'] != password:
                raise ValueError('Неверный пароль!')
            return {'Status': 200, 'msg': "Successfully logged in!", 'user': user_data['username']}