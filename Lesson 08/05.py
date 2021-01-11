# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные 
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата. 


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'Сумма чисел равна: {self.a + other.a} и {self.b + other.b} '

    def __mul__(self, other):
        return f'Произведение чисел равно: {self.a * other.b} и {self.b * other.a} '


cn1 = ComplexNumber(5, 12)
cn2 = ComplexNumber(-3, 20)
print(cn1 + cn2)
print(cn1 * cn2)