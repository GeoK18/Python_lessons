# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Марка машины {self.name}.'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} поворачивает {direction}.'

    def show_speed(self):
        return f'\n Ваша скорость: {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nУ вас слишком высокая скорость! Ваша скорость {self.speed}!'
        else:
            return f'У вас допустимая скорость {self.speed}.'


class SportCar(Car):
    def show_speed(self):
        if self.speed > 100:
            return f'\nУ вас слишком высокая скорость! Ваша скорость {self.speed}!'
        else:
            return f'У вас допустимая скорость {self.speed}.'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nУ вас слишком высокая скорость! Ваша скорость {self.speed}!'
        else:
            return f'У вас допустимая скорость {self.speed}.'


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 50:
            return f'\nУ вас слишком высокая скорость! Ваша скорость {self.speed}!'
        else:
            return f'У вас допустимая скорость {self.speed}.'


town = TownCar('Renault', 60, 'зеленый', False)
print('1: ' + town.go(), town.show_speed(), town.turn('вправо'), town.stop())

sport = SportCar('Ferrari', 270, 'красный', False)
print('\n2: ' + sport.go(), sport.show_speed(), sport.turn('вправо'), sport.stop())

work = WorkCar('VW', 30, 'синий', False)
print('\n3: ' + work.go(), work.show_speed(), work.turn('влево'), work.turn('влево'), work.stop())

police = PoliceCar('Hyndai', 120, 'белый', True)
print('\n4: ' + work.go(), work.show_speed(), work.turn('вправо'), work.stop())
