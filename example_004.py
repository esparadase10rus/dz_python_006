#ДЗ_2, №3
#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Было
#n = int(input('input N: '))
#factorial = 1
#for i in range(1, n+1):
#    factorial *= i
#    print(factorial, end=' ')

#Стало

def faktorial():

    factorial = lambda f : f * factorial(f-1) if f > 0 else 1
    print("Факториал заданного числа равен:", factorial(int(input('Введите число N:\t'))))

faktorial()
