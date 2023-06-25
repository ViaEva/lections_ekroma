import json

file_path = 'data.json'

class GetMixin:
    '''Миксин для обмена ланными с data.json'''
    def get_data(self):
        with open(file_path) as file:
            return json.load(file)

    def get_id(self):
        with open('id.txt','r') as file:
            id = int(file.read())
            id += 1
        with open('id.txt', 'w') as f:
            f.write(str(id))
        return id

class CreateMixin(GetMixin):
    '''Миксин по созданию новых машин'''
    def create_product(self):
        data = super().get_data()
        try:
            new_product = {
                'id': super().get_id(),
                'brand': input('Введите марку машины: '), 
                'model': input('Введите модель машины: '), 
                'year_of_manufacture': int(input('Введите год выпуска машины: ')), 
                'engine_size': round(float(input('Введите объем двигателя машины: ')),1), 
                'color': input('Введите цвет машины: '),
                'body_type': input('Выберите тип кузова (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): '),
                'mileage': int(input('Введите пробег машины: ')),
                'price': round(float(input('Введите цену машины: ')),2)
            }
        except ValueError:
            print('Введите корректные данные!')
            self.create_product()
        else:
            data.append(new_product)
            with open(file_path,'w') as file:
                json.dump(data, file)
            return 'SUCCESSFULL CREATED!'
class ListingMixin(GetMixin):
    '''Миксин по получению списка всех машин'''
    def listing_products(self):
        print('This is listing of product')
        data = super().get_data()
        print(data)
        return 'End'

class RetrieveMixin(GetMixin):
    '''Миксин по получению одной машины по индексу'''
    def retrieve_data(self):
        data = super().get_data()
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Введите корректные данные!')
            return self.retrieve_data()
        else:
            one_car = list(filter(lambda x: x['id'] == id, data))
            if not one_car: return 'Нет такого продукта!'
            else: return one_car[0]

class UpdateMixin(GetMixin):
    '''Миксин по обновлению данных о машине'''
    def update_data(self):
        data = super().get_data()
        flag = False
        try:
            id = int(input('Введите id продукта: '))

        except ValueError:
            print('Введите корректное id!')
            return self.update_data()
        else: 
            one_product = list(filter(lambda x: x['id'] == id, data))
            if not one_product: return 'Такого продукта нет!'
            product = data.index(one_product[0])
            choice = int(input('Что бы вы хотели изменить? (1 - brand, 2 - model, 3 - year of manufacture, 4 - engine size, 5 - color, 6 - body type, 7 - mileage, 8 - price):'))
            if choice == 1: 
                data[product]['brand'] = input('Введите новую марку машины: ')
                flag = True
            elif choice == 2:
                data[product]['model'] = input('Введите новую модель машины: ')
                flag = True
            elif choice == 3:
                try:
                    data[product]['year_of_manufacture'] = int(input('Введите новый год выпуска машины: '))
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 4:
                try:
                    data[product]['engine_size'] = input('Введите новый объем двигателя: ')
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 5:
                data[product]['color'] = input('Введите новый цвет машины: ')
                flag = True
            elif choice == 6:
                data[product]['body_type'] = input('Введите новый тип кузова машины (седан, универсал. купе, хэтчбек, минивен, внедорожник, пикап): ')
                flag = True
            elif choice == 7:
                try:
                    data[product]['mileage'] = int(input('Введите новый пробег машины: '))
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            elif choice == 8:
                try:
                    data[product]['price'] = round(float(input('Введите новую цену машины: ')),2)
                except ValueError: 
                    return 'Введите корректные данные!'
                else:
                    flag = True
            else:
                print('Такого поля нет!')
            with open(file_path,'w') as file:
                json.dump(data, file)
        if flag: return 'SUCCESSFULL UPDATED'
        else: return 'Нет такого продукта!'
class DeleteMixin(GetMixin):
    '''Миксин по удалению машины'''
    def delete_product(self):
        data = super().get_data()
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Введите корректное id!')
            return self.delete_product()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))
        if not one_product: 
            return 'Такого продукта нет!'
        product = data.index(one_product[0])
        data.pop(product)
        
        
        with open(file_path,'w') as file:
            json.dump(data, file)
        return 'SUCCESSFUL DELETED!'

class OrderMixin(GetMixin):
    '''Миксин по выполнению заказов'''
    def order_car(self):
        data = super().get_data()
        list_of_orders = []
        try:
            id = int(input('Введите id продукта: '))
        except ValueError:
            print('Введите корректное id!')
            self.order()
        else:
            one_product = list(filter(lambda x: x['id'] == id, data))[0]
        if not one_product: 
            return 'Такого продукта нет!'
        product = one_product
        print(f'Ваш заказ: {one_product["brand"]} {one_product["model"]}')

        with open(file_path,'w') as file:
            json.dump(data, file)
        return 'Ожидайте ваш заказ!'
class
