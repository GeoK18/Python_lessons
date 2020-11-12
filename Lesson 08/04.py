# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников. 
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class EquipmentStock:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def income(self):
        try:
            name = input(f'Введите наименование: ')
            price = int(input(f'Введите цену: '))
            quantity = int(input(f'Введите количество: '))
            item = {'Модель устройства': name, 'Цена за ед': price, 'Количество': quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print('Недопустимое значение!')


class Printer(EquipmentStock):
    pass


class Scanner(EquipmentStock):
    pass


class Xerox(EquipmentStock):
    pass


pr = Printer('Brother', 12000, 1)
sc = Scanner('Canon', 10300, 14)
xx = Xerox('Xerox', 15800, 20)
pr.income()
sc.income()
xx.income()

