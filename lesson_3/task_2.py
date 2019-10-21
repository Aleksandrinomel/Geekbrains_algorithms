# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
from random import randint as ri

SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 20
first_array = [ri(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
second_array = []

for ind, item in enumerate(first_array):
    if item % 2 == 0:
        second_array.append(ind)

print(f'Первый массив - {first_array}')
print(f'Второй массив - {second_array}')
