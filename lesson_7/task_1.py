# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import numpy.random as rand


def bubble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):  # надеюсь, что под "сделать умнее" подразумевалась замена 1 на n  :)
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1

    return array


array = rand.randint(-100, 100, size=10)
print(array)
print(bubble_sort(array))
