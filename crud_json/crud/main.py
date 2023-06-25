
import json

FILE_PATH = 'data.json'

def get_data():
    with open(FILE_PATH) as file:
        return json.load(file)

def get_id():
    with open('id.txt','r') as file:
        id = int(file.read())
        id += 1
    with open('id.txt','w') as file:
        file.write(str(id))
        return id

def create_prod():
    data = get_data()

    product = {
        'id':get_id(),
        'name': input('vvedite imya produkta: '),
        'price': float(input('vvedite price produkta: ')),
        'discriptiion': input('vvedite opisanie produkta: ')
    }
    data.append(product)

    with open(FILE_PATH,'w') as file:
        json.dump(data,file)

# def delete_product():
#     data = get_data()

#     name = input('DELETE:vvedite imya producta: ')

    