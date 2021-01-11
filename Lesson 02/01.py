# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. 
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

type_int = 7
type_float = 1.5
type_str = "Hello!!!"
type_list = ['a', '1']
type_tuple = ('b', '2')
type_dict = {'Name': 'Tomas', 'Age': '10'}

total = [type_int, type_float, type_str, type_list, type_tuple, type_dict]
for i in total:
    print(f'{i} is {type(i)}')
