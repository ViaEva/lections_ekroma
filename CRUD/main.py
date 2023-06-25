from views import *

def main():
    print('Привет, тебе доступны следующие функции: \n\tLIST-1\n\tRETRIEVE-2\n\tCREATE-3\n\tUPDATE-4\n\tDELETE-5')
    choice = input('Vvedite deistvie(1,2,3,4,5): ')
    if choice == '1':
        list_of_products()
    elif choice == '2':
        detail_retrieve()
    elif choice == '3':
        create_product()
    elif choice == '4':
        update_product()
    elif choice == '5':
        delete_product()
    else:
        print('Invalid choice!!!')
        main()

    ask = input('Hotite prodoljt\'(Yes/No)? ')
    if ask.lower() == 'yes':
        main()
    else:
        print('Пока пока!')

main()
