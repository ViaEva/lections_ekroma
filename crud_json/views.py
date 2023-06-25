import json


FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)


def get_one_data():
    data = get_data()
    id = int(input('Введите id продукта: '))

    element = list(filter(lambda x: x['id'] == id, data))
    
    return element[0]

def post_data():
    data = get_data()
    data.append({
        'id':int(input('vvedi id producta: ')),
        'name': input('imya produkta: '),
        'price': float(input('vvedite price produkta: '))
    })
    with open(FILE_PATH,'w') as file:
        json.dump(data,file)
    return 'CREATED'

def update_data():
    data = get_data()
    id = int(input('vvedite id dlya izmeneniya: '))
    update = list(filter(lambda x: x['id'] == id,data))

    if not update:
        return 'net tokogo'
    
    index_ = data.index(update[0])
    data[index_]['name'] = input('vvedite novoe imya produkta: ')
    data[index_]['price'] = float(input('vvedite new price: '))
    with open(FILE_PATH, 'w') as file:
        json.dump(data,file)

def delete_data():
    data = get_data()
    id = int(input('vvedite id: '))
    delete = list(filter(lambda x: x['id'] == id,data))

    if not delete:
        return 'net tokogo'
    
    index_ = data.index(delete[0])
    data.pop([index_])
    json.dump(data,open(FILE_PATH,'w'))
    return 'DELETED'

    
