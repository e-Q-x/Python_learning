#Написать программу с словарами. Вывод времени года при вводе числа.
# time = int(input("введите число месяца: "))
# month = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень", 10: "осень", 11: "осень", 12: "зима"}
# def play(name):
#     print(month[name])
# result = play(time)


# input_number = input("Введите число: ")
# def get_season(number):
#     if not number.isdigit():
#         print(f"{number}, не является числом")
#         return
#     if 12 < int(number) or int(number) < 1:
#         print(f"{number}, не является месяцем")
#         return
#     month = {
#         (1,2,12): "зима",
#         (3,4,5,12): "весна",
#         (6,7,8): "лето",
#         (9,10,11): "осень",
#     }
#     for key in month:
#         if int(number) in key:
#             print(month[key])
# get_season(number=input_number)



# 2.реализовать задачу  с машинами следующим образм:
# - все машины хранить в списке, информация о каждой машине в словаре.

# cars = []
# car_brand = input("Введите бренд авто:" )
# car_model = input("Введите модель авто:" )
# car_age = input("Введите год машины:" )
# car_color = input("Введите цвет машины:" )
# car1 = {
#     "brand": "bmw",
#     "model": "525",
#     "age": "2019",
#     "color": "blue"
# }
# car2 = {
#     "brand": "audi",
#     "model": "s4",
#     "age": "1992",
#     "color": "red"
# }
# cars.append(car1)
# cars.append(car2)
# # print(cars)
# def add_car(brand, model, age, color):
#     cars.append({
#         "brand": brand,
#         "model": model,
#         "age": age,
#         "color": color
#     })
#
# for i in range(1,4):
#     print(f"введите инфу о машине {i}")
#     car_brand = input("Введите бренд авто:")
#     car_model = input("Введите модель авто:")
#     car_age = input("Введите год машины:")
#     car_color = input("Введите цвет машины:")
#     add_car(car_brand, car_model, car_age, car_color)
#
# print(*cars,sep="\n")

#Пользователь вводит с клавиатуры строку, необходимо вывести на экран, первый символ, полследний символ, кол-во символов.
# Кол-во букв: А, цифр, пробелов, Первые три символа и последние 3 символа. Перевернуть строку 1234(желательно при пмощи срезов)
# add_str = input("Введите любое слово: ")
# string = add_str[0]
# print(string)

# add_str = input("Введите любое слово: ")
# string = add_str[-1]
# print(string)

# add_str = input("Введите любое слово: ")
# string = len(add_str)
# print(string)

# add_str = input("Введите любое слово: ")
# string = add_str.count("a")
# print(string)

# add_str = input("Введите любое слово: ")
# string = add_str.count(" ")
# print(string)

add_str = input("Введите любое слово: ")
string = add_str.count(" ")
print(string)

# add_str = input("Введите любое слово: ")
# string = add_str[:3]
# print(string)

# add_str = input("Введите любое слово: ")
# string = add_str[-3:]
# print(string)