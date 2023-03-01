# class SumMax:
#     def sum_func(a):
#         s = 0
#         while a > 0:
#             s += a % 10
#             a //= 10
#         return s
#     def max_func(a):
#         m = 0
#         while a > 0:
#             if a % 10 > m:
#                 m = a % 10
#             a //= 10
#         return m
# print(SumMax.sum_func(321))
# print(SumMax.max_func(321))

"""Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
Количество повторов добавляется к символам с помощью постфикса формата _n."""
# import random
# default_string = [random.randint(1, 9) for _ in range(10)]
# print(default_string)
# default_dict = {}
# for i in default_string:
#     default_dict[i] = default_dict.get(i, -1) + 1
#     print(i if default_dict.get(i) == 0 else f'{i}_{default_dict.get(i)}', end= ', ') #печатать(i если ключ
                                                                                        #default_dict.get(i) == 0
                                                                                        #иначе i_ключ из словаря
"""import random
my_str = [random.randint(1, 9) for _ in range(10)]
print(my_str)
my_dict = {}
for i in my_str:
    my_dict[i] = my_dict.get(i, 0) + 1
    print(i if my_dict.get(i) == 1 else f'{i}_{my_dict.get(i)}', end=', ')"""

"""Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
слов содержится в этом тексте."""
# users_string = str(input('enter words: ')).lower().split()
# print(len(set(users_string))) #печатать(длину(множество(user_string)))
#
# my_str = input('Enter your words: ')
# print(len(set(my_str.lower().split())))

"""Написать программу, которая состоит 4 из этапов:
- создает список из рандомных четырех значных чисел
- принимает с консоли цифру и удаляет ее из всех элементов списка
- цифры каждого элемента суммирует пока результат не станет однозначным числом
- из финального списка убирает все дублирующиеся элементы
- после каждого этапа выводить результат в консоль
Пример:
- 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
- 2 этап: Введите цифру: 3
- 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
- 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
- 3 этап: [3, 1, 5, 5, 3, 5, 4]
- 4 этап: [3, 1, 5, 4] """

"""# 1
import random
default_string = [random.randint(1000, 9999) for _ in range(6)]
print(default_string)
# 2
n = input('enter a number: ')
# 3
new_string = []
for value in default_string: #пробег по значениям дефолтной строки
    elem = str(value) #задаем значение элемента строкой
    if n in elem: #если введенное число присутствует в элементе
        elem = elem.replace(n,'') #удаляем число из элемента (все в режиме str)
    new_string.append(elem) #добавляем исправленный элемент в новый список
print(new_string)
#4
final_string = []
for value in new_string: #пробег по новому списку
    sum_num = sum([int(elem) for elem in value]) #сложение всех цифр в элементе
    while sum_num > 9: #пока сумма более 9
        sum_num = sum([int(elem) for elem in str(sum_num)]) #складываем цифры
    final_string.append(sum_num) #собираем новый список
print(final_string)
#5
print(set(final_string)) #через множество убираем повторы"""
"""import random
#1
def_str = [random.randint(1000, 9999) for _ in range(6)]
print(def_str)
#2
user_n = input('Enter your number: ')
#3
new_str = []
for value in def_str:
    el = str(value)
    if user_n in el:
        el = el.replace(user_n,'')
    new_str.append(int(el))
print(new_str)
#4
fin_str = []
for value in new_str:
    sum_num = sum(int(el) for el in str(value))
    while sum_num > 9:
        sum_num = sum(int(el) for el in str(sum_num))
    fin_str.append(sum_num)
print(fin_str)
#5
print(set(fin_str))"""

"""Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)"""
"""import random
n = random.randint(100, 999)
print(f'{n} => {sum(int(el) for el in str(n))}')"""

"""Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Пример:
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10"""
"""s_num = input('Enter your number: ')
if int(s_num) % 6 == 0:
    print(f'{s_num} => Peter {int(int(s_num) / 6)}, Kate {int(int(s_num) / 6 * 4)}, Serg {int(int(s_num) / 6)}')
else:
    print('Some one is lying')"""

"""Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no"""
"""import random
ticket_num = random.randint(100000, 999999)
print(ticket_num)
ticket = str(ticket_num)
print('y' if int(ticket[0]) + int(ticket[1]) + int(ticket[2]) == int(ticket[3]) + int(ticket[4]) + int(ticket[5]) else 'n')"""


"""Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:
3 2 4 -> yes
3 2 1 -> no"""
"""n = int(input('Enter n: '))
m = int(input('Enter m: '))
s = int(input('Enter s: '))
print('yes' if s % n == 0 or s % m == 0 else 'no')"""

"""Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""
"""import random
n = int(input('Enter n: '))
coin_base = [random.randint(0,1) for _ in range(n)]
print(coin_base)
orel_1 = 0
resh_2 = 0
for value in coin_base:
    if value > 0:
        orel_1 +=1
    else:
        resh_2 +=1
print('орел' if orel_1 < resh_2 else 'решка')"""

"""Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
"""
"""summ = int(input('Enter sum: '))
mult = int(input('Enter multi: '))
for i in range(1000):
    for j in range(1000):
        if i + j == summ and i * j == mult:
            print(i, j)
            break"""



"""Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N."""

"""n = int(input('Enter limit: '))
i = 1
while i < n:
    print(i, end=' ')
    i*=2"""
