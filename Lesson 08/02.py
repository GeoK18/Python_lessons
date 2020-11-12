# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. 
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        num1 = int(input('Введите делимое: '))
        num2 = int(input('Введите делитель: '))
        if num2 == 0:
            raise ZeroError("На ноль делить нельзя!")
        else:
            res = num1 / num2
            return res
        
    except ValueError:
        return "Ошибка! Вы ввели не число."

    except ZeroError as err:
        return err


print(div())
