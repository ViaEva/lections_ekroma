import random
class Snipers:
  def __init__(self, name, hp, dmg):
    self.name = name
    self.hp = hp
    self.dmg = dmg
  def damaged(self):
    k1 = random.randint(0,12)
    k2 = random.randint(0,6)
    k3 = random.randint(1,3)
    if k2 > 4:
      self.hp -= k1*2/k3
      print('''

      ты кританул                                                 _________
        ______________qooop____                         ____     /         |
       |   _______крит урон   /==[]==========[]  ~~~~~~|____)    |(o)  (O) |
       |___|__/   \_____________/                                |   o     |
                                                                 \_________/        
      ''')
    elif k2 > 2:
      self.hp -= k1/k3
      print('''
      
      ты попал                                           _________
         _______________________                 ___    /         \                        
       {|\_____урон____________/     ===========|___)   |===  === |                                        
        q____   ______________|                         |   __    |                                     
        /    |_/                                        \_________/                                                           
       /    /                                                                       
      /____/                            
      ''')
    else:
        print('''
        
        промах
          _________
         /         \   
         |===  === |   повезло повезло
         | \___/   |
         \_________/  
        ''')
    print(f'''
         урон     {k1}
         Шанс:    {k2}
    Защита врага: {k3}
    
    ''')

p1 = input('введи свое имя Игрок 1: ')
p2 = input('введи свое имя Игрок 2: ')
p3 = input('введи свое имя Игрок 3: ')

def attack():
  try:
    eval(input(f'{i.name}, в кого ты хочешь выстрелить?: ')).damaged()
  except:
      print('norm pishi')
 


snip1 =locals()[p1] = Snipers(p1, 100, 20)
snip2 = locals()[p2] = Snipers(p2, 100, 20)
snip3 = locals()[p3] = Snipers(p3, 100, 20)

res = [snip1, snip2, snip3]
resHp = [snip1.hp, snip2.hp, snip3.hp]
while resHp[0] >= 0:
  resHp = sorted([snip1.hp, snip2.hp, snip3.hp])
  for i in res:
    if i.hp == 0:
      continue
    # try:
    #   eval(input(f'{i.name}, в кого ты хочешь выстрелить?: ')).damaged()
    # except:
    #   prin()
    attack()
    print(f'''
      {snip1.name}:{snip1.hp}
      {snip2.name}:{snip2.hp}
      {snip3.name}:{snip3.hp}
    ''')
else:
  print('игра окончена')
