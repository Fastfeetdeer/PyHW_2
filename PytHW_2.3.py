# Задача 2.3: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input("До какого значения выводить степени 2ки?: "))
i = 0
while 2 ** i <= n:
    print(2 ** i, end=" ")
    i += 1