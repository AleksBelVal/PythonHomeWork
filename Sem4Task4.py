# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена/
# Записать в файл многочлен степени k.    
# Пример:        k=2 => 2*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0

from random import randint
import itertools

k = randint(2, 7)

def get_ratios(k):
    ratios = [randint(0, 10) for i in range (k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10) 
    return ratios

def get_polynom(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x',' x')


ratios = get_ratios(k)
polynom1 = get_polynom(k, ratios)
print(polynom1)

with open('Sem4Task41.txt', 'w') as data:
    data.write(polynom1)

# Второй многочлен для следующей задачи:

k = randint(2, 5)

ratios = get_ratios(k) 
polynom2 = get_polynom(k, ratios)
print(polynom2)

with open('Sem4Task42.txt', 'w') as data:
    data.write(polynom2)
