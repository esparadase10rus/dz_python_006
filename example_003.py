#ДЗ_2, №2
#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.

#Было
#from msilib import sequence

#n = int(input('Введите число: ')) 

#def get_squerence(n):
#    return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]

#nums = get_squerence(n)
#print(nums)
#print(round(sum(nums), 5))

#Стало
n = int(input('Введите число N:\t'))
fc = lambda x: (1 + 1 / x) ** x
numbers = [fc(x) for x in range (1, n + 1)]
print(round(sum(numbers), 3))