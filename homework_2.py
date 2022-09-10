# 14 Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# # Математический способ. Не работает для дробной части(((((((

# n = float(input('Введите число n: '))
# a = int(n)
# b = n - int(n)
# sum = 0
# while b != 0 or a != 0:
#     sum = sum + a % 10 + int(b*10)
#     a //= 10
#     b = b * 10 - int(b*10)
# print("Сумма цифр числа равна: ", sum)

# # Рабочий способ
# num = input('Введите дробное число n: ')
# sum = 0
# for i in num:
#     if i != '.':
#         sum += int(i)
# print(sum)



# 15 Напишите программу, которая принимает на вход число N
#  и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# При помощи словаря
# from math import factorial

# n = int(input('Введите число N: '))
# some_dict = {}
# for i in range(1, n + 1):
#     some_dict[i] = factorial(i)
# print(some_dict)

# N = int(input('Введите число N: '))
# factorial = 1
# for i in range(1, N + 1):
#     factorial *= i
#     print(factorial, end=' ')

# 16 Задайте список из n чисел последовательности $(1+\frac 1 n)^n$
# и выведите на экран их сумму.

# N = int(input('Введите число N: '))
# sum = 0
# for i in range(1, N+1):
#     print((1+(1/i))**i, end=' ')
#     sum = float(sum + round((1 + 1/i)**i, 2))
# print('\n Сумма равна = ', sum)


# 17 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции хранятся в файле file.txt в одной строке одно число.


# from random import *
# N = int(input('Введите число N: '))
# list = []
# for i in range(-N, N+1):
#     list.append(randint(-N, N))
# print(list)

# # Дописала после лекции, всё равно не правильно работает((((((
# f = open('17.txt', 'w')
# for i in range(randint(2, len(list))):
#     f.write(str(randint(8, len(list)-1)) + '\n')
# f.close()

# pr = 1
# with open('17.txt', 'r') as f:
#     for i in f.read().splitlines():
#         pr = pr * list[int(i)]
# print(pr)

# 18 Реализуйте алгоритм перемешивания списка.

# list = [1, 5, 'текст', False, 1.562]
# print(list) 
# import random
# random.shuffle(list)
# print('Перемешанный список:', list) 