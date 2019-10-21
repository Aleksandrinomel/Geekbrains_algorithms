# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint as ri

SIZE = 6
MIN_ITEM = 0
MAX_ITEM = 20
array = [ri(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_num = 0
min_num = 0

for ind, item in enumerate(array):
    if item > array[max_num]:
        max_num = ind
    if item < array[min_num]:
        min_num = ind

print(f'Изначальный массив {array}')
array[min_num], array[max_num] = array[max_num], array[min_num]
print(f'Получившийся массив {array}')

