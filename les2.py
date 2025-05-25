#Логический тип boolean - значения True или False
# is_active = True
# c = 5 > 10
# print(is_active)
# print(c)
#Списки (list)
#         0 1 2 3 4 Индекс начинается с "0"
numbers = [1,2,3,4,5]
my_list = []
print(my_list)
my_list.append("Привет")
print(my_list)
my_list.append(4)
print(my_list[0])
print(len(numbers)) #Функция которая возвращает колличество элементов в колекции
text = "python"
print(len(text))
new_list = [10,11,12]
my_list.append(new_list)
print(my_list)
my_list.extend(new_list)
print(my_list)
print(my_list[2][1])
#Словарь (dict)
#Словарь определяется {}
#Словарь хранит элементы ввиде пар ключ:значение
# {"name": "Дима", "age": 25}
# В словаре не может быть 2 ключа с одинаковыми именами.
# В словаре нет числовых индексов. Кол-во элементов определяется кол-вом пар.
car = {}
person = {"name": "Дима", "age": 25}
#Добавление элемента в словарь
car['brand'] = "bmw"
person['phone'] = '11111'
print(car)
print(person)
#Получение элемента словарая происходит по его ключу
print(person["name"])
