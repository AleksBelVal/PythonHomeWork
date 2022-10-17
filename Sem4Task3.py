# Дана последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

def list1(size, m, n):
    return [randint(m, n) for i in range(size)]

def not_repet_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = list1(size, m, n)
print(origin)
print(not_repet_value(origin))
