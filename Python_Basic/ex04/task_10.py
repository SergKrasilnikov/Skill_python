print('Задача 10. Максимальное число (по желанию)')

# Пользователь вводит три числа.
# Напишите программу,
# которая выводит на экран максимальное из этих трёх чисел (все числа разные).
# Можно использовать дополнительные переменные, если нужно

num1 = int(input('Первое число: '))
num2 = int(input('Второе число: '))
num3 = int(input('Третье число: '))
if num1 > num2:
  max_num = num1
else:
  max_num = num2
if num3 > max_num:
  max_num = num3
print('Максимальное число: ', max_num)