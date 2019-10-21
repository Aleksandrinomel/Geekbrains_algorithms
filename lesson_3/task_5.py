# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.
from random import randint as ri

SIZE = 6
MIN_ITEM = -1
MAX_ITEM = 20
array = [ri(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_neg_number = 0
pos_max_neg_number = None

for ind, item in enumerate(array):
    if max_neg_number == 0 and item < 0:
        max_neg_number = item
        pos_max_neg_number = ind
    elif max_neg_number < item < 0:
        max_neg_number = item
        pos_max_neg_number = ind

if max_neg_number == 0:
    print(f'Максимальный отрицательный элемент отсутствует в массиве')
else:
    print(f'Максимальный отрицательный элемент - {max_neg_number}, его позиция в массиве - {pos_max_neg_number}')