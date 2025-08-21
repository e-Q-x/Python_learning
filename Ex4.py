import json

# range Диапазон
# С их помощью сформировать и вывести на экран числа от 10 до 30
# numbers = list(range (10, 31))
# print(numbers)

#Также с их помощью выведите числа от 5 до 40, которые делятся на 6 без остатка.
# # numbers = list(range(5, 41))
# for i in range(5, 41):
#     if i % 6 == 0:
#         print(i)

# cars = ["bmw", "audi", "honda"] #0 1 2
# for i in range(len(cars)):
#     print(f"{i} {cars[i]}")


# number = input("введите число ")
# if not number.isdigit(): # !!!!!!!!!!!!!
#     print('вы ввели не число')
# else:
#     number = int(number)
#     month = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
#     if number < 3 and number > 0:
#         print("зима")
#     elif number > 3 and number <= 5:
#         print("весна")
#     elif number > 5 and number <=8:
#         print("лето")
#     elif number > 8 and number <=11:
#         print("осень")
#     elif number >11 and number <= 12:
#         print('зима')
#     else:
#         print ("такого месяца нет")


# При помощи цикла for записать в словарь информацию о 5 разных машинах.
# Вводить данные с клавиатуры. Модель, марка, год выпуска, цвет.
# Подумать, как здесь применить и списки, и словари.
# Предложить несколько вариантов хранения информации о 5 машинах
# cars = []
# for i in range(1,6):
#     print(f"введите информацию об {i} из пяти машин ")
#     name_car = input("Введите модель своего авто: ")
#     brand_car = input("Введите марку своего авто: ")
#     age_car = input("Введите год выпуска своего авто: ")
#     color_car = input("Введите цвет своего авто: ")
#     car = [name_car, brand_car, age_car, color_car]
#     # if name_car in cars:
#     #     print("такая машина есть")
#     # else:
#     cars.append(car)
#
#         # cars.append(brand_car)
#         # cars.append(age_car)
#         # cars.append(color_car)
#     print("машина добавлена в список")
# for i in cars:
#     print(i)


# cars = dict()
cars = {}
for i in range(1,6):
    name_car = input("Введите модель своего авто: ")
    brand_car = input("Введите марку своего авто: ")
    age_car = input("Введите год выпуска своего авто: ")
    color_car = input("Введите цвет своего авто: ")
    cars[i] = {
        "brand": brand_car,
        "name": name_car,
        "age": age_car,
        "color": color_car
    }
for k, v in cars.items():
    print(k, v)
print(cars[1])
# with open("cars.json", "w", encoding="utf-8") as file:
#     json.dump(cars, file, indent=2)

# else:
#     cars.update({name_car: brand_car, age_car: color_car})
# print(cars)