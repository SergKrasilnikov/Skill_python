print('Задача 8. Вклады')

# Вклад в банке составляет X рублей.
# Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.

# Определите, через сколько лет вклад составит не менее Y рублей.

# Напишите программу,
# которая по данным числам X, Y, P определяет,
# сколько лет пройдёт, прежде чем сумма достигнет значения Y.

X = int(input('Вклад в банке: '))
Y = int(input('Нужное значение: '))
P = int(input('Ежегодно увеличивается на %: '))
year = 0
while X < Y and X >= 0 and Y >= 0:
  X += ((P * X) / 100) // 1
  year += 1
print(year)