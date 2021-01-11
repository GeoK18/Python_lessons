# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

elements = ['0', '1', '2', '3', '4']
if len(elements) % 2 == 0:
    i = 0
    while i < len(elements):
        el = elements[i]
        elements[i] = elements[i+1]
        elements[i+1] = el
        i += 2
else:
    i = 0
    while i < len(elements) - 1:
        el = elements[i]
        elements[i] = elements[i + 1]
        elements[i + 1] = el
        i += 2
print(elements)


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

 month = int(input("Введите месяц в виде целого числа от 1 до 12:"))
 seasons = {"зима": [1, 2, 12], "весна": [3, 4, 5], "лето": [6, 7, 8], "осень": [9, 10, 11]}

 for el in seasons.keys():
     if month in seasons.get(el):
         print("Ваш месяц относится к времени года", el)
         
 # 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. 
 # Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.   
 
 text = input("Введите предложение: ")
a = text.split(' ')
for i, word in enumerate(a, 1):
    if len(word) > 10:
        word = word[0:10]
    print(f"{i}. {word}")
    
    
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга. 
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.    

numbers = [9, 6, 3, 1]
print(f"Набор натуральных чисел: {numbers} ")
user_number = int(input("Введите значение: "))

c = numbers.count(user_number)
for element in numbers:
    if c > 0:
        i = numbers.index(user_number)
        numbers.insert(i+c, user_number)
        break
    else:
        if user_number > element:
            j = numbers.index(element)
            numbers.insert(j, user_number)
            break
        elif user_number < numbers[len(numbers) - 1]:
            numbers.append(user_number)
print(f"Результат: {numbers}")

"""
6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:

[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
"""

goods = []
while input("Would you like add product? Enter yes/no: ") == 'y':
    number = int(input("Введите количество товара: "))
    features = {}
    while input("Would you like add product parameters? Enter yes/no: ") == 'y':
        feature_key = input("Введите цену товара: ")
        feature_value = input("Введите название товара: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
#goods = [(1, {'name': 'comp', 'price': '11'}), (2, {'name': 'pri', 'price': '22'})]
analitics = {}
for good in goods:
    for feature_key, feature_value in good[1].items():
        if feature_key in analitics:
            analitics[feature_key].append(feature_value)
        else:
         analitics[feature_key] = [feature_value]
print(analitics)



 
