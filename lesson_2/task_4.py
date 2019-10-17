# Найти сумму n элементов следующего ряда чисел:
#  1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите кол-во элементов сложения: '))
elem = 1
sum_elements = 0
for i in range(n):
    sum_elements += elem
    elem /= -2
print(sum_elements)
