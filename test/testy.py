



    
# #     # def buk():
# #     #     bukv = 0
# #     #     for i in text.read():
# #     #         if i.isalpha:
# #     #             bukv += 1
# #     #     return bukv
# #     # def slo():
# #     #     t = text.read().split(' ')
# #     #     slov = 0
# #     #     for i in t:
# #     #         slov += 1 
# #     #     return slov
# #     # def stro():
# #     #     strok = 0
# #     #     for i in text.read():
# #     #         if i.isalpha:    
# #     #             strok += 1
# #     #     return strok
# #     # print(text)
# #     # print('букв',buk())
# #     # print('слов',slo())
# #     # print('строк',stro())
# # with open('texter.txt','r') as text:
# #     slov = 0
# #     bukv = 0
# #     strok = 0
# #     t = text.read().replace('\n',' ').replace('.','').split(' ')
# #     for i in t[:-1]:
# #         slov += 1
# #         bukv += len(i)
# #         for v in i:
# #             if v.isupper():
# #                 strok += 1

# #     print('SLOV: ',slov)
# #     print('BUKV: ',bukv)
# #     print('STROK: ',strok)

# # with open('texter.txt', 'r') as text:
# #     list_ = []
# #     slov = len(text.read().replace('.\n', ' ').split())
# #     text.seek(0,0) 
# #     bukv = len(text.read().replace('.\n', '').replace(' ', ''))
# #     text.seek(0,0) 
# #     strok = len(text.readlines())
    
# #     print(slov)
# #     print(strok)      
# #     print(bukv)

# #     # print(bukv)



    








# # # class Counter:
# # #     def __init__(self):
# # #         self.value = 0

# # #     def inc(self):
# # #         self.value += 1

# # #     def dec(self):
# # #         self.value -= 1

# # # # А этот класс - новый. Наследник Counter
# # # class NonDecreasingCounter(Counter):  # в скобках указан класс-предок
# # #     def dec(self):
# # #         pass

# # #     def inc(self):
# # #         pass
# # # n = NonDecreasingCounter()
# # # n.inc()
# # # n.inc()
# # # print(n.value )
# # # n.dec()
# # # print(n.value)




# # from tkinter import *

# # root = Tk()
# # root.title("Hello World!")
# # root.geometry('300x40')

# # def button_clicked():
# #     print("Hello World!")

# # def close():
# #     root.destroy()
# #     root.quit()

# # button = Button(root, text="Press Me", command=button_clicked)
# # button.pack(fill=BOTH)

# # root.protocol('WM_DELETE_WINDOW', close)

# # root.mainloop()
























# # class ContactList(list):
# #   def __init__(self, *ls):
# #     self.ls = ls

# #   def search_by_name(self, imya):
# #     for ls in self.ls:
# #       return [i for i in ls if imya in i]
    
# # all_contacts = ContactList(['Ivan', 'Maris', 'Olga', 'Ivan Olya', 'Olya Ivan', 'ivan']) 

# # print(all_contacts.search_by_name('Olya'))

# # class Person:
# #   def __init__(self, name, age):
# #     self.name = name
# #     self.age = age

# #   def display(self):
# #     print(self.name, self.age)

# # class Student(Person):
# #     def __init__(self, name, age):
# #        super().__init__(name, age)




# # class ZwezdaMixin:
# #   def zwezda(self, slovo):
# #     res = '*' * (len(slovo) -1)
# #     return slovo[0] + res
        
# # class PasswordMixin:
# #   def pass_gen(self, name, last):
# #     res = []
# #     for v in last, name:
# #         for i in v:
# #             if i in 'aeuoiy':
# #                 res.append(i)
# #     return ''.join(res)

# # class MyUser(ZwezdaMixin, PasswordMixin):
# #   def __init__(self, name, last_name):
# #     self.name = name
# #     self.last = last_name
# #     self.__password = self.pass_gen(name, last_name)

# #   @property
# #   def password(self):
# #     raise Exception('Forbidden')
    
# #   def __str__(self) -> str:
# #     return f'{self.zwezda(self.name)} {self.zwezda(self.last)}'

# # s = MyUser('hello', 'World')
# # print(s)
# # print(s.password)



# class Student(dict):
#   def __init__(self, name, last_name, klass, **notes):
#     self.name = name 
#     self.last = last_name
#     self.klass = klass
#     self.notes = notes

#   def __gt__(self, other) -> bool:
#     print('gt сработал')
#     return sum(self.notes.values()) / len(self.notes) > sum(other.notes.values()) / len(other.notes)

# st1 = Student('Karl', 'Wotson', 10, {'math': 100, 'history': 89, 'literature': 88})
# st2 = Student('James', 'White', 12, {'math': 80, 'history': 100, 'literature': 98})
# st1>st2
# st2>st1










class u:
  def toto(self):
    print('toto')

# t = u()
# t.toto()

def e():
  # t.toto()
  e = u()
  e.toto()
e()