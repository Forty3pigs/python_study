from funcs import *

MAX_PICK = 5

candy = 20
pick = 0
player_1 = [0, 'name']
player_2 = [1, 'name']

player_1[1] = input('Enter your name: ')

player_1, player_2 = initiation(player_1, player_2)

while candy > MAX_PICK:
    print(f'Candies remain: {candy}')
    if player_1[0] == 0 or player_1[0] == 1:
        candy -= player_turn(player_1[1], MAX_PICK)
    elif player_1[0] == 2:
        candy -= easy_bot_turn(player_1[1], MAX_PICK)
    elif player_1[0] == 3:
        candy -= hard_bot_turn(candy, player_1[1], MAX_PICK)
    player_1, player_2 = player_2, player_1

print(f'\nCandies remain {candy}\n{player_1[1]} wins!')
