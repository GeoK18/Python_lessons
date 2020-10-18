# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.


def my_func(x, y, z):

        sequence = [x, y, z]
        total = []
        max_1 = max(sequence)
        total.append(max_1)
        sequence.remove(max_1)
        max_2 = max(sequence)
        total.append(max_2)
        print(f"Ответ: {sum(total)}")

try:
    my_func(int(input("Введите первый аргумент: ")), int(input("Введите второй аргумент: ")), int(input("Введите третий аргумент: ")))
except ValueError:
        print(f"Вы ввели не верное значение.")

