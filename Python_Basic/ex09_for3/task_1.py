print('Задача 1. Календарь')

# Напишите программу,
# которая принимает от пользователя день недели в виде строки и выводит его номер на экран.
#
# Пример:
# Введите день недели: вторник
# Номер дня недели: 2
day = input('Введите день недели: ')
index = 0

for num in ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']:
  index += 1
  if num == day:
    print('Номер дня недели: ', index)
    break