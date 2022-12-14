# Задача: предложить улучшения кода для уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Сформировать список из N членов последовательности. Для N = 5: 1, -3, 9, -27, 81 и т.д.

# import random
# n = int(input('Введите число: '))
# from random import randint
#
# def get_degree(n):
#     return [((-3)**i) for i in range(n)]
#
# n = randint(1, 20)
#
# print (get_degree(n))

# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# from random import randint
#
# def get_dict(n):
#     return {x: 3 * x + 1 for x in range(1, n+1)}
#
# n = randint(5, 20)
#
# print(n)
# print(get_dict(n))

# Подсчитать сумму цифр в вещественном числе.

# from random import uniform
#
# n = round(uniform(1, 100), 3)
# def sum_digit(n):
#     return sum(map(int, list(str(n).replace('.',''))))
#
# print(f'Дано вещественное число {n}')
# print(sum_digit(n))

# Написать программу, получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [1, 2, 6, 24]

# from itertools import accumulate
# import operator
#
# n = int(input('Введите число: '))
#
# def get_prods(N):
#     return list(accumulate([x for x in range(1, n + 1)], operator.mul))
#
# print(get_prods(n))

# Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму.

# n = int(input('Введите число: '))
#
# def get_squerence(n):
#     return [round((1 + 1 / x)**x, 5) for x in range (1, n + 1)]
#
# nums = get_squerence(n)
# print(nums)
# print(round(sum(nums), 5))