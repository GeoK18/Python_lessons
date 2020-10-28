# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

import codecs
print(f'Зарплата меньше 20000 руб.:')
with codecs.open('03_list.txt', 'r', 'utf-8') as f:
    workers = {}
    for line in f:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:

            print(f'{key} - {value} руб.')


summa = 0
count = 0
persons = []
with codecs.open('03_list.txt', 'r', 'utf-8') as file_obj:
    for line in file_obj:
        tokens = line.split(' ')
        if int(tokens[1]) <= 200:
            persons.append(tokens[0])
        summa += int(tokens[1])
        count += 1
result = summa / count

print(f"Средняя ЗП всех сотрудников: {result} руб.")
