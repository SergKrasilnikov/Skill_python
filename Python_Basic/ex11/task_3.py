print('Задача 3. Убийца Steam')

# Напишите программу,
# принимающую на вход размер файла обновления в мегабайтах
# и скорость интернет соединения в мегабайтах в секунду.
#
# Для каждой секунды программа рассчитывает
# и выводит на экран сколько процентов от всего объема уже скачано,
# до тех пор пока не будет скачан весь объем.
# В конце программа должна показать сколько всего секунд заняло скачивание обновления.
# Обеспечьте контроль ввода.
#
# Пример:
#
# Укажите размер файла для скачивания: 123
# Какова скорость вашего соединения? 27
#
# Прошло 1 сек. Скачано 27 из 123 Мб (22%)
# Прошло 2 сек. Скачано 54 из 123 Мб (44%)
# Прошло 3 сек. Скачано 81 из 123 Мб (66%)
# Прошло 4 сек. Скачано 108 из 123 Мб (88%)
# Прошло 5 сек. Скачано 123 из 123 Мб (100%)

while True:
  total_size = float(input('Укажите размер файла для скачивания: '))
  speed = float(input('Какова скорость вашего соединения? '))
  if total_size > 0 and speed > 0:
    break

size = 0
total_time = round(total_size / speed) + 1

for time_loop in range(1, total_time + 1):
  size += speed
  percent = size * 100 / total_size
  if size >= total_size:
    print('Прошло', time_loop, 'сек. Скачано', int(total_size), 'из', int(total_size), 'Мб (100%)')
    break
  print('Прошло', time_loop, 'сек. Скачано', int(size), 'из', int(total_size), 'Мб', '(', round(percent), '%)')
print('Скачивание заняло: ', time_loop, 'секунд')