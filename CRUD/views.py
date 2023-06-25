# CRUD 
# C - create
# R - retrieve
# U - update
# D - delete

data = [
    {'id': 1, 'title': 'Redmi Note 10', 'price': 250, 'description': 'Good phone'},
    {'id': 2, 'title': 'Redmi Note 9', 'price': 150, 'descripton': 'Cheap phone'},
    {'id': 3, 'title': 'Iphone 13 Pro Max', 'price': 1000, 'description': 'great phone'},
]

def get_id():
    id = data[-1]['id']
    id += 1
    return id

def create_product():
    product = {
        'id': get_id(),
        'title': input('Vvedite nazvaniye producta: '),
        'price': float(input('Vvesti price producta: ')),
        'description': input('Vvedite description: ')
    }
    data.append(product)
    print('Created!!')

def list_of_products():
    for product in data:
        print('Id of product:', product['id'])
        print('Title:', product['title'])
        print()

def detail_retrieve():
    id_product = int(input('Vvedite id producta: '))
    try: 
        product = list(filter(
            lambda x: x['id'] == id_product, data))[0]
    except IndexError:
        print('Takogo producta net!')
    else:
        print('Id:', product['id'])
        print('Title:', product['title'])
        print('Description:', product['description'])
        print('Price:', product['price'])
        print()

def update_product():
    id_product = int(input('Vvedite id producta: '))
    flag = False
    try:
        product = list(filter(
        lambda x: x['id'] == id_product,
        data))[0]
    except IndexError:
        print('Takogo producta net!')
    else:
        index = data.index(product)
        choice = input('Chto izmenit\'?(1-title, 2-price, 3-description): ')
        if choice == '1':
            data[index]['title'] = input('Vvedite novyi title: ')
            flag = True
        elif choice == '2':
            data[index]['price'] = input('Vvedite novyi price: ')
            flag = True
        elif choice == '3':
            data[index]['description'] = input('Vvedite novyi description: ')
            flag = True
        else:
            print('Nekorektnyi vybor!!')
    if flag:
        print('Successfully updated!!')
    else:
        print('Not updated!!!')

def delete_product():
    id_product = int(input('Vvedite id producta: '))
    flag = False
    try:
        product = list(filter(
        lambda x: x['id'] == id_product,
        data))[0]
    except IndexError:
        print('Takogo producta net!')
    else:
        index = data.index(product)
        data.pop(index)
        flag = True
    if flag:
        print('Successfully deleted!')
    else:
        print('Not deleted!!!')





