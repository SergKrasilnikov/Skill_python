print('Задача 10.')

#Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
#
# Вводится число N,
# далее еще N − 1 чисел:
# номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.

last_card = int(input('Номер последней карточки: '))
sum_1 = sum_2 = 0
for cards_list_1 in range(1, last_card + 1):
  sum_1 += cards_list_1
for card_list_2 in range(1, last_card):
  num = int(input('Номер имеющейся карты: '))
  sum_2 += num
print('Потерянная карта: ', sum_1 - sum_2)