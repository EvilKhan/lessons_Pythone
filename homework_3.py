# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
# import random
# x = int(input('Введите число Х:'))
# n = int(input('Введите длину списка: '))
# my_list = [random.randint(0,100) for _ in range(n)]
# print(my_list)
# my_list.sort() #сортируем список
# print(my_list)
# near_value_min = None
# near_value_max = None
# near_value = None
# my_dict = {}
# for item in my_list:
#     my_dict[item] = my_dict.get(item, 0) +1
# for i in my_list:
#     if i < x:
#         near_value_min = i
#         i += 1
# for i in my_list:
#     if i > x:
#         near_value_max = i
#         i += 1
#         break
# if x - int(near_value_min) < int(near_value_max) - x:
#     near_value = near_value_min
# else:
#     near_value = near_value_max
# if my_dict.get(x)==None:
#     print(F"ближайшее число {near_value}")
# else:
#     print(F"Число {x} встречается {my_dict.get(x)} раз")


# Вторая задача:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков
# result = None
# scrab_dict = {1: 'AEIOULNSTRАВЕИНОРСТ', 2: 'DGДКЛМПУ', 3: 'BCMPБГЁЬЯ', 4: 'FHVWYЙЫ', 5: 'KЖЗХЦЧ', 8: 'JXШЭЮ', 10: 'QZФЩЪ'}
# scrab_word = input('Введите слово на английском или русском языке: ').upper()
# result = sum([k for i in scrab_word for k, v in scrab_dict.items() if i in v])
# print(F'За это слово вы получаете {result} очков')
