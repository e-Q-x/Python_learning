# Напишите программу, которая запрашивает у пользователя ввод текста.
# Выведите количество символов в тексте на экран.
# Если в тексте больше 10 символов, выведите дополнительно сообщение, что текст большой,
# иначе выведите сообщение что текст маленький
text = input('Введите текст: ')
texT = len(text)
print(texT)
if texT > 10:
    print("текстк большой")
elif texT == 10:
    print('текст нормальный')
else:
    print('текст маленький')