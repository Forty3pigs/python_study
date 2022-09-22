from random import randint


def turn_choise():

    return int(input('Turn choise:\n1 for first turn, 2 for second: ')) - 1


def opp_choise():
    return int(input('Choose yor opponent:\n1 for player, 2 for bot: '))


def dif_choise():
    return int(input('Choose difficulity\n1 for easy, 2 for hard: ')) + 1


def player_turn(name, max_pick):
    return int(input(f'\nNow {name} picks.\nYou can pick from 1 to {max_pick}: '))


def easy_bot_turn(name, max_pick):
    pick = randint(1, max_pick)
    print(f'{name} pick {pick}')
    return pick


def hard_bot_turn(candy, name, max_pick):
    pick = candy % (max_pick + 1)
    if pick == 0:
        pick = randint(1, max_pick)
    print(f'{name} pick {pick}')
    return pick


def initiation(player_1, player_2):
    tc = turn_choise()
    if tc == 0:
        op = opp_choise()
        if op == 1:
            player_2[1] = input('Enter other player name: ')
        elif op == 2:
            df = dif_choise()
            if df == 2:
                player_2 = [df, 'Easy Bot']
            else:
                player_2 = [df, 'Hard Bot']
    else:
        player_1, player_2 = player_2, player_1
        op = opp_choise()
        if op == 1:
            player_1[1] = input('Enter other player name: ')
        else:
            df = dif_choise()
            if df == 2:
                player_1 = [df, 'Easy Bot']
            else:
                player_1 = [df, 'Hard Bot']

    return player_1, player_2
