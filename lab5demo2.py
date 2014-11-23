#Name: Chaise Farrar    Lab Partner:Rebecca Siciliano
#
#Course: CSE 1284       Sec: 10     Date Assigned: 10/1/2014
#
#File name: lab5demo2.py     Date Due: 10/1/2014
#
#Program Description: Create a two player snakes and ladder game
#
#
import random           # import random module for .randint() command


def main():
    sa = 0
    sb = 0
    print("Let's play a game")
    while sa < 100 and sb < 100:
        sa = turn("Player A", sa)
        sb = turn("Player B", sb)
    if sa >= 100:
        input('Player A won!')
    else:
        input('Player B won!')

def turn(player, player_score):
    rnum = random.randint(1, 6)
    total = dice_math(rnum, player_score)
    input('Press enter to roll dice.')
    print("Roll is: ", rnum,'.\t\t', player, " score is: ", total, sep='')
    if rnum == 1 or rnum == 6:
            total = turn(player,total)
    return total


def dice_math(rand, player_score):         # Tallies the score
    player_score += rand       # add score
    # SA CHECK FOR SNAKES OR LADDERS
    if player_score == 24:          # SNAKES
        player_score = 1
    elif player_score == 55 or player_score == 71:
        player_score -= 42
    elif player_score == 88:
        player_score = 67
    elif player_score == 99:
        player_score = 6
    elif player_score == 8:            # LADDERS
        player_score = 31
    elif player_score == 15:
        player_score = 97
    elif player_score == 42:
        player_score = 81
    elif player_score == 66:
        player_score = 87
    return player_score
main()