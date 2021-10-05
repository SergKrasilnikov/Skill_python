print('Задача 9. В обратном порядке')

# Реализуйте программу,
# которая получает на вход четырёхзначное число и выводит его на экран в обратном порядке.
# Само число при этом изменять нельзя, то есть нужно обойтись без переприсваивания.
# Однако можно использовать сколько угодно переменных.
# Пример ввода: 1234.
# Пример вывода: 4321.

num_in = int(input('Ввод: '))
a = num_in % 10
b = ((num_in // 10) % 10)
c = ((num_in // 100) % 10)
d = num_in // 1000
num_out = (a * 1000) + (b * 100) + (c * 10) + d

print('Вывод:', num_out)