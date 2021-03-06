print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:

# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# УМНЫЙ ВАРИАНТ ЗА 7 ИТЕРАЦИЙ

num = int(input('Число мальчика: '))
max_num = 100
min_num = 1
if num <= 0 or num > 100:
  print('Ты жульничаешь, маленький негодник!')
  import sys
  sys.exit()
while True:
  guess = (max_num + min_num) // 2
  print('Твое число равно, меньше или больше, чем число ', guess, '?')
  if guess < num:
    print()
    print(3)
    min_num = guess + 1
  elif guess > num:
    print()
    print(2)
    max_num = guess - 1
  else:
    print()
    print(1)
    break
print('Твое число ', guess, ', мешок с костями!')


#ВАРИАНТ ЗА 7 ИТЕРАЦИЙ, КОГДА ТЫКАЕТ НА КЛАВИШИ

max_num = 100
min_num = 1
while True:
  guess = (max_num + min_num) // 2
  print('Твое число равно, меньше или больше, чем число ', guess, '?')
  num = int(input('Ответ мальчика (1 — равно, 2 — больше, 3 — меньше): '))
  if num == 2:
    print()
    print(3)
    min_num = guess + 1
  elif num == 3:
    print()
    print(2)
    max_num = guess - 1
  else:
    print()
    print(1)
    break
print('Твое число ', guess, ', мешок с костями!')