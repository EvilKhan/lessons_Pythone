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

"""Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
слова разделены одним или большим числом пробелов или символами конца строки.Определите, сколько различных
слов содержится в этом тексте."""
# users_string = str(input('enter words: ')).lower().split()
# print(len(set(users_string))) #печатать(длину(множество(user_string)))

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
#
# # 1
# import random
# default_string = [random.randint(1000, 9999) for _ in range(6)]
# print(default_string)
# # 2
# n = input('enter a number: ')
# # 3
# new_string = []
# for value in default_string: #пробег по значениям дефолтной строки
#     elem = str(value) #задаем значение элемента строкой
#     if n in elem: #если введенное число присутствует в элементе
#         elem = elem.replace(n,'') #удаляем число из элемента (все в режиме str)
#     new_string.append(elem) #добавляем исправленный элемент в новый список
# print(new_string)
# #4
# final_string = []
# for value in new_string: #пробег по новому списку
#     sum_num = sum([int(elem) for elem in value]) #сложение всех цифр в элементе
#     while sum_num > 9: #пока сумма более 9
#         sum_num = sum([int(elem) for elem in str(sum_num)]) #складываем цифры
#     final_string.append(sum_num) #собираем новый список
# print(final_string)
# #5
# print(set(final_string)) #через множество убираем повторы
