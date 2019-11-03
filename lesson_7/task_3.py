# массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import numpy.random as rand


def median(array):
    for i in range(len(array)):
        bigger = 0
        lower = 0
        equally = 0

        for j in range(len(array)):
            if i != j:
                if array[i] == array[j]:
                    if equally % 2 == 0:
                        lower += 1
                    else:
                        bigger += 1
                    equally += 1
                elif array[i] < array[j]:
                    bigger += 1
                else:
                    lower += 1

        if bigger == lower:
            return array[i]


m = 4
size = 2 * m + 1
array = rand.randint(1, 10, size=size)
print(array)
print(f' Медианой массива {array} является {median(array)}')
