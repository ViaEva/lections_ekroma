from views import *
import json



class Car(CreateMixin, UpdateMixin, DestroyMixin):
    data = []
    def save(self):
        self.data.append(self.objects)
        with open('data1.json', 'w') as file:
            json.dump(self.data, file)
        return {'msg': 'saved'}



while True:
    i = input('1 - Создать, 2 - Листинг-Листинг, 3 - Ретрив, 4 - Update, 5 - Delet, end - завершить: ')
    if i == '1':
        p = input('введите Марку авто')
        locals()[p] = Car()
        eval(p).post(mark=p, model=input('введите модель: '), year=int(input('введите год выпуска: ')),engine=round(float(input('введите объем двигателя: ')),1), 
                    color=input('введите цвет: '), body=input('введите тип кузова(варианты: седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): )'), 
                    miliage=int(input('введите пробег: ')), price=round(float(input('введите цену: ')),2))
        eval(p).save()
    elif i == '2':
        listing()
    elif i == '3':
        eval(p).update()
#     elif i == '4':
        
#     elif i == '5':
        
#     elif i == 'end':
#         break
#     else:
#         print('tokogo net')

# smartphones = Product()
# print(smartphones.post(title = 'Iphone 14 Pro Max', description = 'The best new phone!', qty = 5, price = 1300))
# print(smartphones.post(title = 'Redmi Note 10', description = 'The best phone for own price!', qty = 10, price = 300))
# print(smartphones.get())
# print(smartphones.patch(2, title = 'Redmi Note 100'))
# print(smartphones.get_detail(2))
# print(smartphones.delete(2))
# print(smartphones.get())
# print(smartphones.post(title = 'Samsung S22 Ultra', description = 'The best new phone by Samsung', qty = 10, price = 900))
# print(smartphones.save())