# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# import random
# n = int(input('Введите количество монет: '))
# coin_orel = 0
# coin_reshka = 0
# coins = None
# count = 0
# for i in range(n):
#     coins = random.randint(0, 1)
#     print(coins)
#     if coins == 0:
#         coin_orel += 1
#     else:
#         coin_reshka += 1
# print("Перевернуть ", coin_orel if coin_orel < coin_reshka else coin_reshka," монет(ы)")

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

# НИЖЕ сама игра
# import random
# digit_x = None
# digit_y = None
# digit_x = int(random.randint(1, 1000))
# print(digit_x) #самопроверка
# digit_y = int(random.randint(1, 1000))
# print(digit_y) #самопроверка
# summ_s = int(digit_x) + int(digit_y)
# mult_p = int(digit_x) * int(digit_y)
# print(F"Угадайте 2 числа, если X + Y = {summ_s}, а X * Y = {mult_p}")
# user_x = int(input('Введите число X: '))
# user_y = int(input('Введите число Y: '))
# if user_x == digit_x and user_y == digit_y or user_x == digit_y and user_y == digit_x:
#     print('True')
# else:
#     print('False')

#Ниже помогалка
# x = int(input('enter X: '))
# y = int(input('enter Y: '))
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(F"{i}, {j}")

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input('enter a number: '))
# i = 0
# while 2**i <= n:
#     print(2**i)
#     i+=1