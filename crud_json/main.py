from views import *

print('chto vy hotite sdelat? POST,GET,DELETE,PUT,DETAIL ')
while True:
    operation = input('vvedite deystviye: ')
    if operation == 'GET':
        print(get_data())
    elif operation == 'DETAIL':
        print(get_one_data())
    elif operation == 'POST':
        print(post_data())
    elif operation == 'PUT':
        print(update_data())
    elif operation == "DELETE":
        print(delete_data())



