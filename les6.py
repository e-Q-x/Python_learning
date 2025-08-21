# def get_info_user(name, last_name, phone=123):
#     user_info={
#         "name": name,
#         "last_name": last_name,
#         "phone": phone
#     }
#     return user_info
#
# name = input("Введите имя: ")
# last_name = input("Введите отчество ")
# phone = input("Введите свой номер телефона: ")
# info = get_info_user(name,last_name)
# print(info)

# def get_number(x,y,z,w):
#     min_number = min(x,y,z,w)
#     max_number = max(x,y,z,w)
#     sum_number = sum([x,y,z,w])
#     result = {"min": min_number, "max": max_number}
#     return result
#
# min_max = get_number(1,2,3,4)
# print(min_max)


# def get_region_from_number(car_number):
#     regions = {
#         "198": "saint-peterburg",
#         "47": "len_oblast",
#         "05": "dagestan",
#     }
#     reg = car_number[-3:]
#     if reg.isdigit():
#         result = regions.get(reg, "не найдено")
#         print(result)
#     else:
#         correct_reg = car_number[-2:]
#         result = regions.get(correct_reg, "не найдено")
#         print(result)


# get_region_from_number("k520ee98")


# def count_words(text):
#     words = text.split(" ")
#     print(words)
#
#
# count_words("192.168.1.1")

birthday = ["11", "01", "98"]
# name = "anton"
# last_name = "ivanov"
# father_name = "sergeevich"
# # birthday_string = birthday[0]+"."+birthday[1]+"."+birthday[2]
# # y = name, last_name, father_name
# fio = " ".join([last_name, name, father_name])
# print(fio)
# brand, model, color = "bmw", "525", "black"
# print(brand)
# x = 5
# y = 10
# x, y = y, x
# print(x)

# def hello():
#     name = "sergey"
#     age = "23"
#     return name, age
# name, age = hello()
# print(name, age)