# Напишить программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16];

list1 = [2, 3, 6, 4, 3, 5]

import math 
size = math.ceil(len(list1)/2)
print(size)
list2 = []
for i in range(size):
    list2.append(list1[i]*list1[-i - 1])

print(list2)
