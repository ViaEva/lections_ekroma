import random

ls = ['Plov', 'Manty', 'Kuurdak', 'Lagman', 'Pelmeni']
pl = 0
m = 0
k = 0
l = 0
pe = 0

for x in range(0, 100000):
    choice = random.choice(ls)
    print(choice)
    if choice.lower() == 'plov':
        pl = pl + 1 # pl += 1 инкремент
    elif choice.lower() == 'manty':
        m += 1
    elif choice.lower() == 'kuurdak':
        k += 1
    elif choice.lower() == 'lagman':
        l += 1
    elif choice.lower() == 'pelmeni':
        pe += 1

print(f'Plov: {pl}, Manty: {m}, Kuurdak: {k}, Lagman: {l}, Pelmeni: {pe}')
# print(f'Победило блюдо: {winner}, оно набрало: {winner}') max()


