'''Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.'''
# a  = int(input())
# b  = int(input())
# for i in range (a, b+1):
#     print(i, end=" ")

# a = int(input())
# b = int(input())
# if a < b:
#     for i in range(a, b + 1):
#         print(i, end=" ")
#
# else:
#     for i in range(a, b - 1, -1):
#         print(i, end=" ")


# a = int(input())
# b = int(input())
# for i in range(a - (a + 1) % 2, b - b % 2, -2):
#     print(i, end=" ")
'''Дано 10 целых чисел. Вычислите их сумму. Напишите программу, использующую наименьшее число переменных.'''
# sum = 0
# for i in range(10):
#     number = int(input())
#     sum += number
# print(sum)

'''Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
Какое наименьшее число переменных нужно для решения этой задачи?'''
# number = int(input())
# sum = 0
# for i in range(number):
#     number = int(input())
#     sum += number
# print(sum)

'''По данному натуральному n вычислите сумму 13+23+33+...+n3.'''
# n = int(input())
# k = 0
# for i in range(n + 1):
#     k += (i ** 3)
# print(k)

'''Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.

По данному натуральному n вычислите значение n!. Пользоваться математической библиотекой math в этой задаче запрещено.
'''
# number = int(input())
# p = 1
# for i in range(number):
#     p *= (i+1)
# print(p)
'''По данному натуральном nn вычислите сумму 1!+2!+3!+...+n!1!+2!+3!+...+n!. В решении этой задачи можно использовать
 только один цикл. Пользоваться математической библиотекой math в этой задаче запрещено.'''

# n = int(input())
# partial_factorial = 1
# partial_sum = 0
# for i in range(1, n + 1):
#     partial_factorial *= i
#     partial_sum += partial_factorial
# print(partial_sum)

'''Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

Sample Input 1:

5
0
700
0
200
2
Sample Output 1:

2
'''
# s=0
# n=int(input())
# for i in range(n):
#     n=int(input())
#     if n == 0:
#         s=s+1
# print(s)

'''По данному натуральному n ≤ 9 выведите лесенку из n ступенек, i-я ступенька состоит из чисел от 1 до i без 
пробелов.'''
# n = int(input())
# # for i in range(1, n + 1):
# #     for j in range(1, i + 1):
# #         print(j, sep='', end='')
# #     print()
#
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()

'''Задача «Потерянная карточка»

Условие
Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась. Найдите ее, зная номера 
оставшихся карточек.
Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N). Программа должна вывести номер 
потерянной карточки.
Для самых умных: массивами и аналогичными структурами данных пользоваться нельзя.
Sample Input 1:
5
1
2
3
4
Sample Output 1:

5'''

# n = int(input())
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# for i in range(n - 1):
#     sum -= int(input())
# print(sum)

