print('Задача 6')

# Реализуйте программу,
# которая запрашивает два числа у пользователя.
# После этого у каждого числа возьмите две последние цифры.
# Получившиеся два числа сложите и выведите на экран.

# Пример:
# Введите первое число: 456
# Введите второе число: 123
# Сумма: 79

first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))

n1 = first % 10
n2 = second % 10

print(n1 + n2)