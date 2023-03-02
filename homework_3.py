# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
# import random
# list_len = int(input('ВВеди длину списка: '))
# our_number = int(input('Введи число: '))
# our_list = [random.randint(1,100) for _ in range(list_len)]
# print(our_list)
# our_dict = {}
# min_list = [abs(our_number - el) for el in our_list]
# min_ind = min_list.index(min(min_list))
# for item in our_list:
#     our_dict[item] = our_dict.get(item, 0) + 1
# if our_dict.get(our_number) is None:
#     print('ближайшее значение', our_list[min_ind])
# else:
#     print(f'{our_number} встречается {our_dict.get(our_number)} раз')


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
# result = 0
# for i in scrab_word:
#     for key, value in scrab_dict.items():
#         if i in value:
#             result += key
# print(F'За это слово вы получаете {result} очков')
