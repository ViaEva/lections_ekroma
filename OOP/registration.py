import json

File = 'jsondb/users.json'

class RegistrationMixin:
    'Миксин для регистрации Юзера'
    def validate_password(self, password, password2):
        if len(password) < 8:
            raise ValueError('пароль слишком короткий!')
        elif password.isdigit() or password.isalpha():
            raise ValueError("Пароль должен состоять из букв и цифр!!!")
        elif password != password2:
            raise ValueError('Пароли не совпали!!')
    def register(self, username, password, password2):
        self.validate_password(password, password2)

        with open (File, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1]['id'] + 1 
            except (IndexError, ValueError):
                id = 1
                data= []

        with open(File, 'w') as file:
            if data:
                is_username_used = any([x['username']==username for x in data])
                if is_username_used:
                    json.dumb(data, file)
                    raise ValueError ('Такой пользователь уже есть!')
            
            data.append({'id': id, 'username': username, 'password': password})
            json.dump(data, file)
            return {'status': 201, 'msg': 'successfully registered'}

class LoginMixin:
    'миксин для логининга'
    def login(self, username, password):
        with open(File, 'r') as file:
            data = json.load(file)
            is_registered = any([x for x in data])
            if not is_registered:
                raise Exception('нет токого юзера')

            user_data = list(filter(lambda x: x['username'] == username, data))[0]
            if user_data['password'] != password:
                raise ValueError('неверный пороль')

            return {'status': 200, 'msg': 'soccessfully logged in ','user': user_data['username']}

class User(RegistrationMixin,LoginMixin):
    pass

user = User()
print(user.register('JohnSnow','john1234','john1234'))


def call_function(func):
    print('Вызываю функцию', func()) 
    func()   
    print(f'Вызов функции {func()} прошёл успешно')
    
@call_function
def first():
    print("hello world")
    return "hello world"
first()


#Вызываю функцию first
# hello world 
# Вызов функции first прошёл успешно 

