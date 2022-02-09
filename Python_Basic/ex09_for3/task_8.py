print('Задача 8. Колонтитул')

# Нам нужно написать программу для печати важных объявлений.
# Сверху объявления должен располагаться вот такой колонтитул:
#  ~~~~~~~~~~!!!!!!~~~~~~~~~~
# Восклицательные знаки всегда располагаются по центру строки,
# причём в зависимости от важности объявления количество восклицательных знаков может быть разным.
#
# Напишите программу,
# которая спрашивает у пользователя сначала общую длину колонтитула в символах,
# потом желаемое количество восклицательных знаков,
# после чего выводит на экран готовую строку.

long = int(input('Длина колонтитула: '))
exclamation_marks = int(input('Кол-во восклицательных знаков: '))

print('~' * ((long - exclamation_marks) // 2) + '!' * exclamation_marks + '~' * ((long - exclamation_marks) // 2))