# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве. 
# Пример: - A (3,6); B (2,1) -> 5,09
3
xA = float(input('Введите координату х точки А'))
yA = float(input('Введите координату y точки А'))
xB = float(input('Введите координату x точки B'))
yB = float(input('Введите координату y точки B'))

length = ((xA-xB)**2+(yA-yB)**2)**0.5
length = int(length * 100)/100
print(length)