#ДЗ_2, №1
#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Было
#float_num = input('input float number: ')
#print(type(float_num))
#sum = 0
#for i in float_num:
#    if i != '.':
#         sum += int(i)
#print(sum)

# Стало

from functools import reduce

n = input("Введите вещественное число: ").replace(',', '')
m = list(map(int, n))
print(f'Сумма цифр числа равна', reduce(lambda x, y: x + int(y), m))