# Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
start = 32
stop = 127
k = 0

for i in range(start, stop + 1):
    print(f' {i}-{chr(i)}', end='')
    k += 1
    if k % 10 == 0:
        print()
