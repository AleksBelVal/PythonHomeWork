# Программа принимает на вход цифру, обозначающее день недели
# и проверяет, является ли этот день выходным

day = int(input('Введите цифру от 1 до 7, обозначающее день недели: '))
if day < 1 or day > 7:
    print('Не правильно введена цифра')
elif day == 6 or day == 7:
    print('Это выходной день')
else:
    print('Нет, это не выходной день')