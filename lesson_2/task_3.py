# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.


number = int(input('Введите целое число: '))
revers_number = 0
while number > 0:
    revers_number = revers_number * 10 + number % 10
    number = number // 10
print(revers_number)
