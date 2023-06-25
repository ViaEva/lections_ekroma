'''
select - выборка данных
select * from table_name; - выборка всех полей
select column_name from table_name - выборка указанных полей 

where - фильтрация данных
select * from table_name where condition

Операторы сравнения:
> - больше 
< - меньше 
= - сравнение 
>=
<=
!= or <> - неравенство

and - и
or - или
in - в
between - между
like - подходит ли под шаблон(с учетом регистра)
ilike - без учета регистра
'%a%' - в слове есть буква а
'a%' - слово начинается с а
'%a' - слово заканчивается на а
'_' - _ озночает кол-во символов

is null - проверка на пустое значение
not - отрицание условия 
limit - лимит
order by - сортировка по полю
desc - по убыванию
ask - по возростанию
group by - групирует по

update - обновление данных
UPDATE table_name SET column_name=value, column_name2=value2 WHERE condition;

delet -  удаление данных
delet from table_name; - очистка всей таблицы
delet from table_name where condition; - очистка данный подходящих под условие

insert into - добовление данных
insert into table_name (colum_names) values (values_for_colums);

функции в PostgressSQL

АГРЕГАЦИОННЫЕ ФУНКЦИИ:
COUNT() - функция для счета количества вхождений 
AVG() - функция для поиска среднего значения
MAX() - функция для поиска максимального значения
MIN() - функция для поиска минимального значения
SUM() - функция для поиска результата сложения всех значений 

|| ' ' || - конкатенация

case when - постоновка значений в зовисимости от условия
select first_name, case when title_of_courtesy like 'Mr.' then 'Male' else 'Female' end as gender from employees;



join - связи между таблицами
full join - соеденяются все таблицы
left join - соеденение из левой таблицы 
right join - соеденение из правой таблицы
inner join - соеденение только тех данных, которые имеют пересечение

select * from person join pets

input:
select  per.name, pet.name from person as per join pets as pet on per.person_id=pet.pet_id;

output:
  name  | name  
--------+-------
 kairat | tuzik




input:
select e.first_name || ' ' || e.last_name as employee_name,
count(c.company_name),
sum(o.freight)
from orders as o
join employees as e
on o.employee_id=e.employee_id
join customers as c
on o.customer_id=c.customer_id
group by employee_name;

output:

  employee_name   | count |    sum    
------------------+-------+-----------
 Robert King      |    72 | 6665.4404
 Nancy Davolio    |   123 |  8836.639
 Laura Callahan   |   104 | 7487.8804
 Michael Suyama   |    67 | 3780.4695
 Andrew Fuller    |    96 |  8696.408
 Steven Buchanan  |    42 | 3918.7104
 Janet Leverling  |   127 | 10884.737
 Margaret Peacock |   156 | 11346.138
 Anne Dodsworth   |    43 | 3326.2598

impor:
psql data_base_name < sql_name

export:
pg_dump database_name > sql_name



'''