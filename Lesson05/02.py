# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.

my_list = ['Hi\n', 'all\n', 'people\n', 'in\n', 'the world\n']
with open("list02.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)
with open("list02.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = len(line)-1
        print(f"{letters} букв в строке")
    print(f"Всего {lines} строк.\n")
with open("list02.txt") as file_obj:
    print(f"Список слов в файле:")
    print(file_obj.read())
