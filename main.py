#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)
digit = input('Введите трехзначное число: ')
result = int(digit[0]) + int(digit[1]) + int(digit[2])
print(digit,'->',result)