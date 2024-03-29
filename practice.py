import random

"""Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""

# n = random.randint(100, 999)
# n = str(n)
# print(n)
# print(sum(int(k) for k in n))

"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10"""

# s = int(input('Сколько журавликов? : '))
# if s%6==0:
#     print(f'{s} -> {int(s/6)}  {int(s/6*4)}  {int(s/6)}')
# else:
#     print('кто то врет')

"""Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no"""

# tick_num = random.randint(100000, 999999)
# tick_num = str(tick_num)
# print(tick_num)
# if int(tick_num[0]) + int(tick_num[1]) + int(tick_num[2]) == int(tick_num[3]) + int(tick_num[4]) +int(tick_num[5]):
#     print('yes')
# else:
#     print('no')
# print('yes' if sum(int(i) for i in tick_num[:3]) == sum(int(i) for i in tick_num[3:]) else 'no') #однострочие

"""Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один 
разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no"""

# n = int(input('Введите длину шоколадки: '))
# m = int(input('Введите ширину шоколадки: '))
# k = int(input('Сколько отломить?: '))
# if (k % n == 0 or k % m == 0) and k < n * m:
#     print('yes')
# else:
#     print('no')

"""На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной 
и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
"""

# n = int(input('Введи количество монеток: '))
# coins = [random.randint(0, 1) for _ in range(n)]
# print(coins)
# coin_0 = 0
# coin_1 = 0
# for c in coins:
#     if c > 0:
#         coin_1 += 1
#     else:
#         coin_0 += 1
# print(coin_0 if coin_0 < coin_1 else coin_1)

"""Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

# from discriminant import discriminant
# s = int(input('Введите сумму: '))
# p = int(input('Введите произведение: '))
# print(discriminant.discr(1, -s, p))

"""Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

# n = int(input('Введите число: '))
# i = 1
# while i < n:
#     print(i, end=' ')
#     i*=2

"""Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению"""

# list_len = int(input('Введите длину списка: '))
# my_num = int(input('Какое число ищем?: '))
# my_list = [random.randint(1, 100) for _ in range(list_len)]
# print(my_list)
# my_dict = {}
# for item in my_list:
#     my_dict[item] = my_dict.get(item, 0) + 1
# min_list = [abs(my_num - el) for el in my_list]
# print(min_list)
# min_ind = min_list.index(min(min_list))
# if my_dict.get(my_num) is None:
#     print('nearest number ', my_list[min_ind])
# else:
#     print(my_dict.get(my_num), 'раз встречается число в списке')
# list_len = int(input('Введи длину списка: '))
# f_num = int(input('Какое число искать? '))
# def_list = [random.randint(1, 100) for _ in range(f_num)]
# print(def_list)
# our_dict = {}
# for elem in def_list:
#     our_dict[elem] = our_dict.get(elem, 0) + 1
# min_list = [abs(el - f_num) for el in def_list]
# print(min_list)
# min_index = min_list.index(min(min_list))
# if our_dict.get(f_num) is None:
#     print('ближайшее число ', def_list[min_index])
# else:
#     print(F'число {f_num} встречается {our_dict.get(f_num)} раз(а)')

"""В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка;
B, C, M, P – 3 очка;
F, H, V, W, Y – 4 очка;
K – 5 очков;
J, X – 8 очков;
Q, Z – 10 очков.
А русские буквы оцениваются так:
А, В, Е, И, Н, О, Р, С, Т – 1 очко;
Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка;
Й, Ы – 4 очка;
Ж, З, Х, Ц, Ч – 5 очков;
Ш, Э, Ю – 8 очков;
Ф, Щ, Ъ – 10 очков"""

# scrab_dict = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# scrab_word = input('Enter numb word: ').upper()
# for l in scrab_word:
#     for k,v in scrab_dict.items():
#         if l in v:
#             result_count+=k
# print(result_count)
#print(sum(k for l in scrab_word for k,v in scrab_dict.items() if l in v)) #однострочный вариант


"""Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""

# n = int(input('Введи длину первого списка: '))
# m = int(input('Введи длину второго списка: '))
# list_1 = [random.randint(1, 9) for _ in range(n)]
# list_2 = [random.randint(1, 9) for _ in range(m)]
# print(list_1)
# print(list_2)
# list_1.sort()
# list_2.sort()
# print(set(list_1))
# print(set(list_2))
# final_list = []
# for i in list_1:
#     for l in list_2:
#         if i == l:
#             final_list.append(i)
# print(final_list)

"""В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте 
выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля 
и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки."""

# number_of_bushes = int(input('Введите кол-во кустов: '))
# bed_of_blueberries = [random.randint(1,9) for _ in range(number_of_bushes)]
# print(bed_of_blueberries)
# three_bushes = 0
# sums_of_blueberries =[]
# for berry in range(len(bed_of_blueberries)-1):
#     three_bushes = bed_of_blueberries[berry -1] + bed_of_blueberries[berry] + bed_of_blueberries[berry+1]
#     sums_of_blueberries.append(three_bushes)
# sums_of_blueberries.append(bed_of_blueberries[-2] + bed_of_blueberries[-1] +bed_of_blueberries[0])
# print(sums_of_blueberries)
# print(max(sums_of_blueberries))

# n = int(input('Введи предел фибоначчи: '))
# fib_list = [1, 1]
# fib_1 = fib_2 = 1
# i = 0
# for i in range(2, n):
#     fib_1, fib_2 = fib_2, fib_1 + fib_2
#     fib_list.append(fib_2)
#
# print(fib_2)

# def fibbonacci(n):
#     if n in[1,2]:
#         return 1
#     else:
#         return fibbonacci(n-2) + fibbonacci(n - 1)
#
# print(fibbonacci(10))

"""заменить максимальные значения списка на минимальные"""
# n = int(input('Enter n: '))
# list_def = [random.randint(1, 5) for _ in range(n)]
#
# for i in list_def:
#     if list_def[i] > 3:
#         list_def[i] = random.randint(1, 3)
# print(list_def)

"""простое или нет число"""
# def is_prime(numb):
#     if numb % 2 == 0:
#         return numb == 2
#     d = 3
#     while d * d <= numb and numb % d != 0:
#         d += 2
#     return d * d > numb
# print(is_prime(int(input("Enter numb number: "))))

"""Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 """

# def degree_of(numb, pow):
#     if pow == 0:
#         return 1
#     return numb * degree_of(numb, pow - 1)
#
#
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(f'А = {a}; В = {b} -> {degree_of(a, b)}')

"""Напишите рекурсивную функцию sum(numb, pow), возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4 """

"""def sum(a, b):
    if b == 0:
        return a
    a += 1
    b -= 1
    return sum(a, b)


print(sum(3, 10))"""

"""Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

# a_1 = int(input('Введите первый элемент: '))
# d = int(input('Введите разность: '))
# n = int(input('Введите количество элементов: '))
# for i in range(n):
#     print(a_1+i*d)

"""Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)"""
# my_list = [random.randint(1, 99) for _ in range(10)]
# n_min = int(input('Введите минимум: '))
# n_max = int(input('Введите максимум: '))
# print(my_list)
# for i in range(len(my_list)):
#     if n_min <= my_list[i] <= n_max:
#         print(i, end=' ')