# # from abc import ABC, abstractmethod
# # from math import pi

# # class Shape(ABC):
# #     def __init__(self, name):
# #         self.name = name

# #     @abstractmethod
# #     def area(self):pass

# #     def fact(self):
# #         print('Я фигура в 2 мерной плоскости')

# # class Square(Shape):
# #     def __init__(self,lenght):
# #         super().__init__('квадрат')
# #         self.lenght = lenght
# #     def area(self):
# #         return self.lenght ** 2

# #     def fact(self):
# #         super().fact()
# #         print(f'я {self.name}, у меня все углы 90 град')

# # class Circle(Shape):
# #     def __init__(self, radius):
# #         super().__init__('Circle')
# #         self.radius = radius

# #     def area(self):
# #         return pi * self.radius ** 2

# # a = Square(4)
# # print(a.area())
# # a.fact()

# # b = Circle(3)
# # print(b.area())
# # b.fact()


# ###############################################################################


# # class ChessPiece(ABC):
# #     def draw(self):
# #         print('Drew a chess piece')

# #     @abstractmethod
# #     def move(self):pass

# # from datetime import date

# # current_date = date.today()
# # print(current_date)


# import datetime 

# # def last_day_of_month(any_day): 
# #     next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
# #     return next_month # this will never fail return next_month - datetime.timedelta(days=next_month.day

# # print(last_day_of_month(datetime.date.today()))
# # import datetime

# def last_day_of_month(any_day):
#     next_month = any_day.replace(day=28) + datetime.timedelta(days=4) 
#     return next_month - datetime.timedelta(days=next_month.day)

# print(last_day_of_month(datetime.date.today()).strftime('%d'))

# from abc import ABC, abstractmethod
# import datetime

# class DaysAndDates(ABC):
#   @abstractmethod
#   def define_date(self):
#     pass
    
#   @abstractmethod
#   def define_days(self):
#     pass

# class Current:
  
#   def define_date(self):
#     return datetime.datetime.today().strftime('%d-%m-%y')
    
#   def define_days(self):
#     return 'А тут че вводить не сказано'

# class MonthStart:
#   t_d = int(datetime.datetime.today().strftime('%d'))
#   def define_date(self):
#     return datetime.datetime.today().strftime(f'{self.t_d - (self.t_d-1)}-%m-%y')

#   def define_days(self):
#     return f'С начала месяца прошло {self.t_d-1} дней'

# class MonthEnd:
#   next_month = datetime.date.today().replace(day=28) + datetime.timedelta(days=4) 
#   res = (next_month - datetime.timedelta(days=next_month.day))
  
#   def define_date(self):
#     return self.res.strftime('%d-%m-%y')
    
#   def define_days(self):
#     r = int(self.res.strftime('%d')) - int(datetime.datetime.today().strftime('%d'))
#     return f'до последнего дня еще {r} дней'

# cr = Current()
# fr = MonthStart()
# ls = MonthEnd()

# print(cr.define_date())
# print(cr.define_days())
# print()
# print(fr.define_days())
# print(fr.define_date())
# print()
# print(ls.define_date())
# print(ls.define_days())



'''
2. Создайте абстрактный класс Car с методом get_info. Создайте класс Toyota и переопределите
 метод get_info так, чтобы метод выводил информацию о типе автомобиля, пробеге и стоимости.
'''
# from abc import ABC, abstractmethod

# class Car(ABC):
#   @abstractmethod
#   def get_info(self):
#     pass

# class Toyota(Car):
#   def get_info(self):
#     return 'легковушла, пробег 100, 200000'

# t = Toyota()
# print(t.get_info())


# '''
# 3. Создайте абстрактный класс Bank с атрибутами экземпляра класса name, interest_rate, term,
#  loan_balance, interest_balance и методами: get_product, loan_issue, interest_accrual и loan_repayment.
# а) Создайте класс StartupLoan, переопределите метод get_product, чтобы он выводил информацию о кредитном продукте:
# Кредитный продукт: “Стартап”
# Процентная ставка: 20% годовых
# Срок кредита: 2 года
# b) Добавьте методы:
# - loan_issue для выдачи кредита, который увеличивает сумму loan_balance и выводит сообщение “Кредит в сумме {сумма} сомов выдан {дата} года.”
# - interest_accrual для начисления процентов со дня выдачи до конца месяца с выводом информации “Задолженность по процентам: {interest_balance} сомов”
# - loan_repayment для погашения основной суммы и процентов с выводом информации: “Кредит погашен в сумме {сумма}. Остаток по кредиту: {loan_balance} сомов,
# #  остаток по процентам: {interest_balance} сомов.”

# К абстрактным методам добавить док-стринг с описанием методов.
# '''
# from abc import ABC, abstractmethod
# import datetime

# class Bank(ABC):
#   def __init__(self, name, interest_rate, term, loan_balance, interest_balance=0):
#     self.name = name
#     self.i_r = interest_rate
#     self.term = term
#     self.l_b = loan_balance
#     self.i_b = interest_balance

#   @abstractmethod
#   def get_product(self):
#     pass

#   @abstractmethod
#   def loan_issue(self):
#     pass


#   @abstractmethod
#   def interest_accrual(self):
#     pass

#   @abstractmethod
#   def loan_repayment(self):
#     pass

# class StartupLoan(Bank):
#   def get_product(self):

#     return f'Кредитный продукт: {self.name}\nПроцентная ставка: {self.i_r} годовых\nСрок кредита: {self.term} года'

#   def loan_issue(self):
#     return f'Кредит в сумме {self.l_b} сомов выдан {datetime.datetime.today().strftime("%Y")} года.'

#   def interest_accrual(self):
#     i = int(input('введите кол-во пройденных дней(в числах): '))
    
#     self.i_b = self.l_b * self.i_r/100/365*i

#     return f'Задолженность по процентам: {self.i_b} сомов'

#   def loan_repayment(self):
#     p_c = int(input('введите сумму погошения кридита'))
#     p_p = int(input('введите сумму погошения процентов'))
#     cred_res = self.l_b - p_c
#     proc_res = self.i_b - p_p
#     return f'Кредит погашен в сумме {p_c}. Остаток по кредиту: {cred_res} сомов,остаток по процентам: {proc_res} сомов.'

# st = StartupLoan(input('введите имя компании: '),int(input('введите процентную ставку: ')),int(input('срок: ')),int(input('сумма денЯг: ')))

# while True:
#     i = input('1 - увидеть общую инфу, 2 - инфа по кредиту, 3 - инфа по Задолженность по процентам, 4 - погасить сумму, end - завершить: ')
#     if i == '1':
#         print(st.get_product())
#     elif i == '2':
#         print(st.loan_issue())
#     elif i == '3':
#         print(st.interest_accrual())
#     elif i == '4':
#         print(st.loan_repayment())
#     elif i == 'end':
#         break
#     else:
#         print('tokogo net')

class Makers:
  students_count = 0
  def __init__(self, name, language, kpi):
    self.name = name
    self.lang = language
    self.kpi = kpi

  def add_stud(self):
    Makers.students_count += 1

  def info(self):
    print(f'name: {self.name}, language: {self.lang}')

  def kpi(self, kpi):
    self.kpi = kpi

while 1 != 0:
  i = input('1 - add Student, 2 - info, 3 - count, 4 - end ')
  if i == '1':
    p = input('name eng: ')
    l = input('language: ')
    k = int(input('Kpi: '))
    locals()[p] = Makers(p,l,k)
    locals()[p].add_stud()
  elif i == '2':
    eval(input('vvedite imya')).info()
  elif i == '3':
    print(Makers.students_count)
  elif i == '4':
      break