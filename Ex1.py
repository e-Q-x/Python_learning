# Написать программу, в которой пользователь вводит с клавиатуры свои имя, фамилию,
# отчество, возраст, номер телефона. Добавить эти данные в словарь.
# Вывести весь словарь на экран. Вывести на экран только имя и фамилию
name = input("Введите имя: ")
surname = input("Введите фамилию:")
surname2 = input("Введите отчество:")
age = int(input("Введите возраст:"))
phone = int(input("Введите номер телефона:"))
person = {}
person["name"] = name
person["surname"] = surname
person["surname2"] = surname
person["age"] = age
person["phone"] = phone
print(person)
print(person["name"], person["surname"])

