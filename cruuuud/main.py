from views import *
import json

class Car(CreateMixin, ListingMixin, RetrieveMixin, UpdateMixin, DeleteMixin, OrderMixin):
    def start(self):
        choice = input('Добро пожаловать!\nХотите начать работу? Да/Нет: ')

a = Car()
a.start()

while choice.lower() == 'да':
    print('Что бы вы хотели сделать?(1 - create, 2 - listing, 3 - retrieve, 4 - update, 5 - delete, 6 - order, 7 - exit)')
    a = int(input('Выберите действие: (1,2,3,4,5,6,7): '))
    if a == 1: print(super().create_product())
    elif a == 2: print(.listing_products())
    elif a == 3: print(super().retrieve_data())
    elif a == 4: print(super().update_data())
    elif a == 5: print(super().delete_product())
    elif a == 6: print(super().order_car())
    elif a == 7: 
        print('Благодарим вас за работу!')
        break
    else: print('Такого действия нет!')



