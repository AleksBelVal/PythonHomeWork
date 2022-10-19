# Игра для 2х игроков. Дано N конфет. 
# Каждый игрок, по очереди, за ход может взять не более M конфет.
# Побеждает игрок, забравший последнюю конфету.
# man vs man

import random

rules = ('Игра "Забери все конфеты!" '
    'Правила игры: '
    'В игре участвуют два игрока'
    'Выбираем на какое количество конфет будет игра, '
    'Выбираем какое количество конфет можно брать за один ход, '
    'Выигрывает тот, кто заберёт последнюю конфету.')
            

talk = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def play_game(n, m, players, talk):
    count = 0
    if n%10 == 1 and 9 > n > 10: letter = 'а'
    elif 1 < n%10 < 5 and 9 > n > 10: letter = 'ы'
    else: letter = ''
    while n > 0:
        print(f'{players[count%2]}, {random.choice(talk)}')
        move = int(input())
        if move > n or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0: print(f'Осталось {n} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(rules)

player1 = input('Давайте знакомиться. Первый игрок, как Вас зовут?\n')
player2 = input('Второй игрок, Ваше имя? \n')
players = [player1, player2]

n = int(input('Сколько конфет будет разыгрываться?\n '))
m = int(input('Определим, какое максимальное количество конфет можно взять за один ход?\n '))

winer = play_game(n, m, players, talk)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! Победил {winer}! Ему достаются все конфеты!')