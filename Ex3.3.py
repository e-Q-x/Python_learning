# Дан словарь {“a1”:1, “b1”:2, “a2”:3, “b2”:4, “a3”:6}
# 1. Выведите элементы, у которых ключ начинается с буквы а
# 2. Выведите элементы, у которых значения четные числа
# 3 выведите элементы, у которых соблюдены оба условия
# 4 выведите элементы, у которых соблюденj одно из  условия
numbers = {'4a':7, 'a1':1, 'b1':2, 'a2':3, 'b2':4, 'a3':6}
# for i in numbers:
#     if "a" == i[0]:
#         print(f"ключ = {i}, значение = {numbers[i]}")
# for key, value in numbers.items():
#     if value % 2==0:
#         print(value)
for key, value in numbers.items():
    is_even = value % 2 == 0
    if "a" == key[0] or (value % 2==0 and value > 2):
        print(key, value)
        if value % 2==0:
            print(key, value)
