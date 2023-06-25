import json

file_path = 'data.json'

class GetMixin:
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
            with open(File,'w') as file:
                json.dump(data, file)
            return 'SUCCESSFULL CREATED!'
class ListingMixin(GetMixin):
    def listing_products(self):
        print('This is listing of product')
        data = super().get_data()
        print(data)
        return 'End'

class RetrieveMixin(GetMixin):
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
                data[product]['mark'] = input('Введите новую марку машины: ')
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
                data[product]['body_type'] = input('Введите новый тип кузова машины (сед

# import json
# from search import search_object

# class CreateMixin:
#     def post(self, **kwargs):
#         with open('id.txt', 'r') as file:
#             id = int(file.read())
#             id += 1
#         with open('id.txt', 'w') as file:
#             file.write(str(id))
#         object_ = dict(id=id, **kwargs)
#         self.objects = []
#         self.objects.append(object_)
#         return {'status': 201, 'msg': object_}

# class UpdateMixin:
#     def update(self):
#         id = int(input('Введите id продукта: '))
#         with open('data1.json') as file:
#             product = list(filter(lambda x: x['id'] == id, json.load(file)))
#         data = json.load(file)

#         if not product:
#             print('Такого продукта нет')

#         index_ = data.index(product[0])
#         choice_ = int(input('что вы хотите изменить? 1 - Марка, 2 - Модель, 3 - описание, 4 - год выпуска, 5 - цена: '))

#         if choice_ == 1:
#             data[index_]["mark"] = input('Введите новую марку: ')
#             flag = True

#         elif choice_ == 2:
#             data[index_]["model"] = input('Введите новую модель: ')
#             flag = True

# def catalog(v):
    for i in v:
        print(f'''
            ID             : {i["id"]}
            Марка          : {i["mark"]}
            Модель         : {i["model"]}
            Год выпуска    : {i["year"]}
            Объем двигателя: {i["engine"]}
            Цвет           : {i["color"]}
            Кузов          : {i["body"]}
            пробег         : {i["miliage"]}
            Цена           : {i["price"]}
            '''   
#         )

#         elif choice_ == 3:
#             data[index_]["year"] = input('Введите новую дату выпуска: ')
#             flag = True
# def catalog(v):
#     for i in v:
#         print(f'''
#             ID             : {i["id"]}
#             Марка          : {i["mark"]}
#             Модель         : {i["model"]}
#             Год выпуска    : {i["year"]}
#             Объем двигателя: {i["engine"]}
#             Цвет           : {i["color"]}
#             Кузов          : {i["body"]}
#             пробег         : {i["miliage"]}
#             Цена           : {i["price"]}
#             '''   
#         )


#         elif choice_ == 4:
#             data[index_]["discription"] = input('Введите новое описание: ')
#             flag = True

#         elif choice_ == 5:
#             data[index_]["price"] = input('Введите новую цену: ')
#             flag = True
        
#         else:
#             print('Такого поля нет')

#         self.data = data

# class DestroyMixin:
#     @search_object
#     def delete(self, id, **kwargs):
#         obj = kwargs['object_']
#         if not obj:
#             return {'status': 404, 'msg': 'Not Found!'}
#         self.objects.remove(obj)
#         return {'status': 204, 'msg': 'Successfully deleted!'}


# def catalog(v):
#     for i in v:
#         print(f'''
#             ID             : {i["id"]}
#             Марка          : {i["mark"]}
#             Модель         : {i["model"]}
#             Год выпуска    : {i["year"]}
#             Объем двигателя: {i["engine"]}
#             Цвет           : {i["color"]}
#             Кузов          : {i["body"]}
#             пробег         : {i["miliage"]}
#             Цена           : {i["price"]}
#             '''   
#         )

# def listing():
#     with open('data1.json','r') as file:
#          for i in eval(file.read()):
#             catalog(i)