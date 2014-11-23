__author__ = 'Chaise'
card_chosen = []
card_flipped = ['moew', 'bark', 'meow', 'quack', 'quack', 'bark' ]
def main():
    play_game = input('Would you like to play a game? (Y or N): ')
    if play_game == ['Y', 'y', 'yes']:
        letsPlay()
    else:
        input('Too bad! Maybe next time....')
def letsPlay():
    global play_game
    for c in range(3):
