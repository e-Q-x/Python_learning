person = {"name": "name1", "age": "age1"}
yes = input("Привет, ты готов сыграть в игру ?: ")
if yes == "да":
    print("Давай познакомимся по ближе")
    name1 = input("Назови свое имя: ")
    person["name"] = name1
    age1 = input("Сколько тебе лет?: ")
    person["age"] = age1
    print("Давай начнем", [name1])
    print("Загадайте число от 1 до 100, на все вопросы отвечайте только да или нет")
    number = input("Это число больше 50: ?")
    if number = "да":
        

else:
    print("Жаль,буду ждать тебя снова")
