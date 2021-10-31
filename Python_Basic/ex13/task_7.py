print('Задача 7. Яйца')

# В рамках программы колонизации Марса
# компания «Спейс Инжиниринг» вывела особую породу черепах,
# которые, по задумке, должны размножаться, откладывая яйца в марсианском грунте.
# Откладывать яйца слишком близко к поверхности опасно из-за радиации,
# а слишком глубоко — из-за давления грунта и недостатка кислорода.
# Вообще, факторов очень много,
# но специалисты проделали большую работу и предположили,
# что уровень опасности для черепашьих яиц рассчитывается по формуле
# D = x**3 − 3x**2 − 12x + 10,
# где x — глубина кладки в метрах,
# а D — уровень опасности в условных единицах.
#
# Для тестирования гипотезы
# нужно взять пробу грунта на безопасной, согласно формуле, глубине.
#
# Напишите программу,
# находящую такое значение глубины "х", при котором уровень опасности как можно более близок к нулю.
# На вход программе подаётся максимально допустимое отклонение уровня опасности от нуля,
# а программа должна рассчитать приблизительное значение "х",
# удовлетворяющее этому отклонению.
#
# Известно, что глубина точно больше нуля и меньше четырёх метров.
#
# Обеспечьте контроль ввода.
#
# Пример:
# Введите максимально допустимый уровень опасности: 0.01
#
# Приблизительная глубина безопасной кладки: 0.732421875 м

max_rate = float(input('Введите максимально допустимый уровень опасности: '))
depth_min = 0
depth_max = 4

depth = depth_min + (depth_max - depth_min) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_rate < 0:
  print('Ошибка')
else:
  print('Глубина:', depth, 'Опасность:', danger)
  while abs(danger) >  max_rate:
    if danger > 0:
      depth_min = depth
    else:
      depth_max = depth
    depth = depth_min + (depth_max - depth_min) / 2
    danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    print('Глубина:', depth, 'Опасность:', danger)

print('Приблизительная глубина безопасной кладки:', depth, 'м')