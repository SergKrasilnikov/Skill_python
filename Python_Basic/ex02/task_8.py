print('Задача 8. Обмен значений двух переменных')

# Что нужно сделать
# Дана программа, которая запрашивает у пользователя два слова, а затем выводит их на экран два раза.

a = input('Введите первое слово: ')
b = input('Введите второе слово: ')
print(a,b)
a, b = b, a
print(a,b)


# Задача: поменять значения переменных a и b местами.
# Изменять, удалять, менять местами 6-ю, 7-ю, 8-ю и последнюю строчки нельзя.
# Но в 9-ю строку можно вставлять сколько угодно кода, не трогая последний принт.
# Пример результата работы программы:

# Введите первое слово: Сок
# Введите второе слово: Вода
# Сок Вода
# Вода Сок