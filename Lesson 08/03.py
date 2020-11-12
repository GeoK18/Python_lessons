# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами. 
# Класс-исключение должен контролировать типы данных элементов списка.


class NumberError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_number
        while True:
            try:
                try:
                    user_number = int(input('Введите число: '))
                    stop = input(f'Число "{user_number}" добавлено в список. Для продолжения "Enter", для остановки "stop". ').lower()
                    self.my_list.append(user_number)
                    if stop == 'stop':
                        print(self.my_list)
                        break
                except ValueError:
                    raise NumberError
            except NumberError:
                stop = input(f'Вы ввели не число! Для продолжения "Enter", для остановки "stop". ').lower()
                if stop == 'stop':
                    print(f'Список введенных чисел - {self.my_list}')
                    break
                else:
                    self.check_value()



a = TypeCheck()
a.check_value()
