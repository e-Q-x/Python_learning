# Кортеж- не изменяемый список.
names = ("Егор", "Антон", "Валера")
print(type(names))
names2 = ["Егор", "Антон", "Валера"]
print(type(names2))
# Строковый тип данных - любая последовательность данных.
text = "i_love_python"
print(type(text))
#Множество- не упорядоченная структура которая хранит только уникальные элементы.
# Определяется как и вловарь {}
numbers = {1,1,1,2,2,3,4,5}
print(numbers)
cars = ["bmw", "bmw", "honda", "jeep"]
uniq_cars = list(set(cars))
print(uniq_cars)
