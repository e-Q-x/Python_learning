#Циклы применяются для многократного выполнения блока кода.
#Циклы бывают условные и без условные
# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     print(i**4)

# cars = ["audi", "bmw", "porsh"]
# for car in cars:
#     print(car, len(car), sep="\n")
# text = "python"
# for i in text:
#     print(i, end="-")
# person = {"name": "misha", "age": 23}
# for i in person:
#     print(i, person[i])
person = {"name": "misha", "age": 23}
# print(person.keys())
# print(person.values())
# print(person.items())
for key, value in person.items():
    print(key, value)