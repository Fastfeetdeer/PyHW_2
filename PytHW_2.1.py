# Задача 2.1: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

import random

n_coins = int(input("Укажите количество монет на столе: ")) 
coins_side = [random.randint(0, 1) for i in range(n_coins)] # позиция монет: 0 - орлом, 1 - решкой
print(coins_side)
orel = 0 # количество поворотов орлов, для решек
reshka = 0 # количество поворотов решек, для орлов
for i in range(len(coins_side)):
    if coins_side[i] == 0: orel += 1
    elif coins_side[i] == 1: reshka += 1
print("Переверните следующее количество монет: ", min(orel,reshka), " для выполнения задачи.")