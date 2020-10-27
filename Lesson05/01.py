# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_list = []
while True:
    line = input("Введите слово. Окончание ввода - пустая строка: ")
    if line == '':
        print(my_list)
        exit()
    else:
        newline = line + '\n'
        my_list.append(newline)

    with open("list.txt", "w") as my_file:
        my_file.writelines(my_list)
