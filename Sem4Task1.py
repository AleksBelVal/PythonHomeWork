# Вычислить число c заданной точностью d    
# Пример:    при d = 0.001,  π = 3.141,   10^(-1) ≤ d ≤10^(-10)
# Формула Бэйли — Боруэйна — Плаффа
import math
from math import pi

n = pi
d =  int(input("Введите число для заданной точности числа Пи:"))

print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')
