print('Задача 8. Сумма ряда')

# Дано натуральное число N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N

N = int(input('Натуральное число: '))
results = 0
for num_list in range(0, N + 1):
  S = (-1) ** num_list * (1/2 ** num_list)
  results += S
print(results)