# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint

numbers = []   # Делаем рандом 10 чисел от 0 до 99
for i in range(10):
    numbers.append(randint(0, 99))
print(numbers)

out_f = open("04_output.txt", 'w')  # Записываем полученные рандомы в файл
list = numbers
out_f.write(str(list))
out_f.close()

in_f = open("04_output.txt", 'r')  # Читаем числа из файла

summ = 0  # суммируем числа, выводим результат суммы на экран
for x in numbers:
    summ += x

print(f'Сумма чисел: {summ}')
in_f.close()

