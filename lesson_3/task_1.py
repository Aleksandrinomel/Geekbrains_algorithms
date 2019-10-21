# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

START_NUM = 2
END_NUM = 99
START_DIVIDER = 2
END_DIVIDER = 9


for i in range(START_DIVIDER, END_DIVIDER + 1):
    number_of_multiple_numbers = 0
    for j in range(START_NUM, END_NUM):
        if j % i == 0:
            number_of_multiple_numbers += 1
    print(f'Числу {i} кратно {number_of_multiple_numbers} чисел')

