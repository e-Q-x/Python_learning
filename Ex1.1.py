#Написать программу, в которой пользователь вводит с клавиатуры три марки машины.
# Добавить эти значения в список. Вывести весь список на экран.
# Вывести отдельно первый элемент (начальный)
model1 = input("Введите марку первой машины:")
model2 = input("Введите марку второй машины:")
model3 = input("Введите марку третей машины:")
list=[]
list.append(model1)
all_list = [model2, model3]
list.extend(all_list)
print(list)
print(list[0])