# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
# Необходимо предусмотреть условие его завершения.

from itertools import count
from itertools import cycle


def count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)


def cycle_func(my_list, iteration):
    i = 0
    el = cycle(my_list)
    while i < iteration:
        print(next(el))
        i += 1


count_func(start_number=int(input("Введите начальное значение:")), stop_number=int(input("Введите конечное значение:")))
cycle_func(my_list=[1, 2, 3, 4, 5], iteration=int(input("Введите значение итератора: ")))
