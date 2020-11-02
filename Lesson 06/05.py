# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Конструктор автомобиля:'


class Color(Car):
    def draw(self):
        return f'Выберите {self.title}'


class Horse(Car):
    def draw(self):
        return f'Выберите {self.title}'


class Door(Car):
    def draw(self):
        return f'Выберите {self.title}'


color = Color('цвет')
print(color.draw())
horse = Horse('мощность')
print(horse.draw())
door = Door('количество дверей')
print(door.draw())
