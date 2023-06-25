from views import *
import json

class Product(CreateMixin,RetrieveMixin,UpdateMixin,DestroyMixin):
    def save(self):
        with open('data.json' , 'w') as file:
            json.dump(self.objects , file)
        return {'msg': 'Saved!'}

class Order:
    discount = 10
    def __init__(self):
        self.orders = []
        self.product = Product()
        self.product.post(title = 'Iphone Pro max', describtion = 'the bset phone' , qty = 5 , price = 1300)
        self.product.post(title = 'Samsung 11a', description = 'the bset phone', qty = 10, price = 400 )

    def create_order(self, objects):
        ls = []
        for item in objects:
            for product in self.product.objects:
                if item['id'] == product['id']:
                    self.substract_qty(item, product)
                    ls.append({'title': product['title'], 'qty': item['qty'], 'price':product['price']})
        self.orders.append(ls)
        money = self.total_count(ls)
        return {'order': ls, 'Total sum': money}

    def total_count(self, objects):
        total_count = 0
        for product in objects:
            price = product['price']
            qty = product['qty']
            total_count += self.make_discount(price, self.discount) * qty
        return total_count

    def substract_qty(self, item, product):
        result = product['qty'] - item['qty']
        if result < 0:
            raise Exception('Too many qty of product')
        product['qty'] = result

    def make_discount(self, price, percent):
        return price - (price/100*percent)

