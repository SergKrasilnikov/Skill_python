print('Задача 9. Недоделка')

# реализуйте игры «Камень, ножницы, бумага» и «Угадай число».
#
# Правила игры «Камень, ножницы, бумага»:
# программа запрашивает у пользователя строку
# и выводит победил он или проиграл.
#
# Камень бьёт ножницы, ножницы режут бумагу, бумага кроет камень.
#
# Правила игры “Угадай число”:
# программа запрашивает у пользователя число до тех пор, пока он его не отгадает.

# ПРОГРАММУ МОЖНО РЕШИТЬ БЕЗ МОДУЛЯ random, ПУТЕМ ВВОДА ЗНАЧЕНИЙ (ПРИМЕР): str1 = ножницы str2 = бумага И СРАВНЕНИЕ ЗНАЧЕНИЙ ЧЕРЕЗ if. ПРЕДЛАГАЮ РЕШИТЬ ЭТУ ПРОГРАММУ ЧЕРЕЗ ИГРУ ПОЛЬЗОВАТЕЛЯ С КОМПЬЮТЕРОМ ЧЕРЕЗ ГЕНЕРАЦИЮ СЛУЧАЙНЫХ ЧИСЕЛ И ПЕРЕВОДА ИХ В НУЖНЫЕ ЗНАЧЕНИЯ

from random import randint


def rock_paper_scissors():
    print('\nИгра «Камень, ножницы, бумага»\n')
    while True:
        man = int(input('Введите число: 1 - камень; 2 - ножницы; 3 - бумага \n'))
        guess = randint(1, 3)

        if guess == man:
            print('Еще раз!\n')
        elif guess == 1 and man == 2:
            print('Компьютер показывает "камень"')
            print('Компьютер выиграл\n')
        elif guess == 1 and man == 3:
            print('Компьютер показывает "камень"')
            print('Игрок выиграл\n')
        elif guess == 2 and man == 1:
            print('Компьютер показывает "ножницы"')
            print('Игрок выиграл\n')
        elif guess == 3 and man == 1:
            print('Компьютер показывает "бумагу"')
            print('Компьютер выиграл\n')
        elif guess == 2 and man == 3:
            print('Компьютер показывает "ножницы"')
            print('Компьютер выиграл\n')
        elif guess == 3 and man == 2:
            print('Компьютер показывает "бумагу"')
            print('Игрок выиграл\n')
        else:
            break


# ПРОГРАММА ВЗЯТА ИЗМОДУЛЯ 6. В ДАННОМ СЛУЧАЕ ОНА РЕШЕНА СПОСОБОМ, КОГДА С ПРОГРАММОЙ НЕ НУЖНО ВЗАИМОДЕЙСТВОВАТЬ И ОНА САМА ОПРЕДЕЛЯЕТ, СООТВЕТСТВУЕТ ЧИСЛО ЗАГАДАННОЕ ПОЛЬЗОВАТЕЛЕМ УГАДЫВАЕМОМУ КОМПЬЮТЕРОМ

def guess_the_number():
    print('\nИгра «Угадай число.»\n')
    num = int(input('Число мальчика (от 1 до 100): '))
    max_num = 100
    min_num = 1
    guess = 0

    while True:
        if num <= 0 or num > 100:
            print('Ты жульничаешь, маленький негодник!')
            break
        guess = (max_num + min_num) // 2
        print('Твое число равно, меньше или больше, чем число ', guess, '?')
        if guess < num:
            print()
            print('Нэт')
            min_num = guess + 1
        elif guess > num:
            print()
            print('Нэт')
            max_num = guess - 1
        else:
            print()
            print('Нэт')
            break
    if guess > 0 and guess <= 100:
        print('Твое число ', guess, '\n')


def mainMenu():
    while True:
        menu = 0
        print()
        while menu < 1 or menu > 2:
            menu = int(input('Выберете игру. 1 - «Камень, ножницы, бумага»; 2 - «Угадай число».'))
            if menu == 1:
                rock_paper_scissors()
            elif menu == 2:
                guess_the_number()


mainMenu()