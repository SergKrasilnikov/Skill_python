print('Задача 10. За что?')

# Напишите программу которая выбирает из двух чисел наибольшее не используя
# при этом условных операторов, циклов и встроенную функцию max.
#
# Пример:
#
# Введите первое число: 10
# Введите второе число: 5
#
# Наибольшее число: 10

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

max_num = (a + b + abs(a - b)) / 2

print('Наибольшее число: ', max_num)