# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

enterprises = defaultdict(int)
n = int(input("Введите кол-во предприятий: "))
for _ in range(n):
    name = input("Введите название предприятия: ")
    for i in range(1, 5):
        enterprises[name] += int(input(f"Введите прибыль компании {name} за {i} месяц"))

average = sum(enterprises.values()) / n
print(f'Средняя прибыль для всех предприятий составляет: {average}')
above_average = []
below_average = []
for key, value in enterprises.items():
    if value > average:
        above_average.append(key)
    if value < average:
        below_average.append(key)
print(f'Предприятия, чья прибыль выше среднего: {", ".join(above_average)}')
print(f'Предприятия, чья прибыль ниже среднего: {", ".join(below_average)}')

