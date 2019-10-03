# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

alfabet = 'abcdefghijklmnopqrstuvwxyz'

letter_1 = input('введите первую букву')
letter_2 = input('введите вторую букву')

letter_1_position = alfabet.find(letter_1) + 1
letter_2_position = alfabet.find(letter_2) + 1
letters_between = abs(letter_1_position - letter_2_position) - 1

print(f'Позиция первой буквы в алфавите - {letter_1_position}')
print(f'Позиция второй буквы в алфавите - {letter_2_position}')
print(f'Колличество букв между ними - {letters_between}')
