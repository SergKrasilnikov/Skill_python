print('Задача 9. Аннуитетный платёж')

# Кредит в сумме S млн руб.,
# выданный на n лет под i% годовых,
# подлежит погашению равными ежегодными выплатами в конце каждого года,
# включающими процентные платежи и сумму в погашение основного долга.
#
# Проценты начисляются в один раз в год.
# После выплаты третьего платежа
# достигнута договорённость между кредитором и заёмщиком
# о продлении срока погашения займа на n_2 лет
# и увеличении процентной ставки с момента конверсии до i_2%.
#
# Напишите программу,
# которая выводит план погашения оставшейся части долга.
#
# A = KS
#
# K = i(1 + i) ** n / (1 + i) ** n - 1
#
# Пример:
#
# Введите сумму кредита: 40e6
# На сколько лет выдан? 5
# Сколько процентов годовых? 6
#
# Период: 1
#
# Остаток долга на начало периода: 40000000.0
# Выплачено процентов: 2400000.0
# Выплачено тела кредита: 7095856.02
#
#
# Период: 2
#
# Остаток долга на начало периода: 32904143.98
# Выплачено процентов: 1974248.6387999998
# Выплачено тела кредита: 7521607.3812
#
# Период: 3
#
# Остаток долга на начало периода: 25382536.5988
# Выплачено процентов: 1522952.195928
# Выплачено тела кредита: 7972903.824072
#
# Остаток долга: 17409632.774728
#
# =================================================
#
# На сколько лет продляется договор? 2
# Увеличение ставки до: 10
#
# Период: 1
#
# Остаток долга на начало периода: 17409632.774728
# Выплачено процентов: 1740963.2774728
# Выплачено тела кредита: 3751267.5625271997
#
# Период: 2
#
# Остаток долга на начало периода: 13658365.2122008
# Выплачено процентов: 1365836.52122008
# Выплачено тела кредита: 4126394.3187799198
#
# Период: 3
#
# Остаток долга на начало периода: 9531970.89342088
# Выплачено процентов: 953197.0893420881
# Выплачено тела кредита: 4539033.750657911
#
# Период: 4
#
# Остаток долга на начало периода: 4992937.142762969
# Выплачено процентов: 499293.71427629696
# Выплачено тела кредита: 4992937.125723703
#
# Остаток долга: 0.017039266414940357

def payment(S, year, percent):
  percent = percent / 100
  K = (percent * (1 + percent) ** year) / ((1 + percent) ** year - 1)
  a_payment = round(K * S, 2)

  return a_payment

def period_printout(S, percent, a_payment, period):
  for period_loop in range(1, period + 1):
    paid_percent = S * percent / 100
    credit_body = a_payment - paid_percent
    print('\nПериод', period_loop)
    print('\nОстаток долга на начало периода:', S)
    print('Выплачено процентов:', paid_percent)
    print('Выплачено тела кредита:', credit_body)
    S -= credit_body
  else:
    print('\nОстаток долга:', S)
    print('\n==============================================')
  return S


S = float(input('Введите сумму кредита: '))
year = int(input('На сколько лет выдан? '))
percent = float(input('Сколько процентов годовых? '))

a_payment = payment(S, year, percent)
new_summ = period_printout(S, percent, a_payment, 3)

new_year = int(input('\nНа сколько лет продляется договор? '))
new_percent = float(input('Увеличение ставки до: '))
new_year = new_year + year - 3

a_payment = payment(new_summ, new_year, new_percent)
new_summ = period_printout(new_summ, new_percent, a_payment, new_year)