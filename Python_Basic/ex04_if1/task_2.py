print('Задача 2. Поступление')

# Напишите программу,
# которая запрашивает у пользователя результаты ЕГЭ по трём экзаменам
# и проверяет, поступил он в институт или нет.
# Выведите соответствующее сообщение.

# Пример:
# Введите кол-во баллов по русскому языку: 90
# Введите кол-во баллов по математике: 90
# Введите кол-во баллов по информатике: 90
# Поздравляю, ты поступил на бюджет!

# Пример 2:
# Введите кол-во баллов по русскому языку: 100
# Введите кол-во баллов по математике: 50
# Введите кол-во баллов по информатике: 70
# К сожалению, ты не прошёл на бюджет.

exam1 = int(input('Введите кол-во баллов по русскому языку: '))
exam2 = int(input('Введите кол-во баллов по математике: '))
exam3 = int(input('Введите кол-во баллов по информатике: '))
summ = exam1 + exam2 + exam3

if (summ >= 270):
    print('Поздравляю, ты поступил на бюджет!')
else:
    print('К сожалению, ты не прошёл на бюджет.')
