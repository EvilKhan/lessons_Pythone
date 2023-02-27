# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random
x = int(input('Введите число Х:'))
n = int(input('Введите длину списка: '))
my_list = [random.randint(0,100) for _ in range(n)]
print(my_list)
my_list.sort() #сортируем список
print(my_list)
near_value_min = None
near_value_max = None
near_value = None
my_dict = {}
for item in my_list:
    my_dict[item] = my_dict.get(item, 0) +1
for i in my_list:
    if i < x:
        near_value_min = i
        i += 1
for i in my_list:
    if i > x:
        near_value_max = i
        i += 1
        break
if x - int(near_value_min) < int(near_value_max) - x:
    near_value = near_value_min
else:
    near_value = near_value_max
if my_dict.get(x)==None:
    print(F"ближайшее число {near_value}")
else:
    print(F"Число {x} встречается {my_dict.get(x)} раз")




