import codecs

# Открываем файл на чтение и разбиваем построчно.
file = codecs.open('05_list.txt', 'r', 'utf-8')
onstring = file.read().split("\n")[:-1]
# получаем список
print(f'Получили список -> {onstring} \n')

dict = dict()  # создаём словарь из списка

print(f'Общее количество часов по предмету:')
for item in onstring:
    key = item.split(" ")[0]
    value = [int(s) for s in item.split() if s.isdigit()]  # вынимаем числа из словаря и присваем значения
    dict[key] = value

    summ = 0  # суммируем числа, выводим результат суммы на экран
    for x in value:
        summ += x
    print(f'{key} {summ} часов.')

file.close()

print(f'\nСловарь на основании которого считалась сумма занятий-> {dict} ')
