# Name: Chaise Farrar       Date Assigned:9/24/2014
#
# Course: CSE 1284 Sec 10   Date Due: 9/24/2014
#
# File name:Card Matching Game
#
# Program Description: Print a selection of cards, allow the user to pick on and see if user can match cards.
print('Lets play a game')
num1=1
num2=2
num3=3
num4=4
num5=5
num6=6
bark=0
meow=0
quack=0
win=0
user=()
count=0
def reprintcard():
    global meow
    global bark
    global quack
    global num1
    global num2
    global num3
    global num4
    global num5
    global num6
    if meow==1:
        num1='Meow'
        num3='Meow'
    if bark==1:
        num2='Bark'
        num6='Bark'
    if quack==1:
        num4='Quack'
        num5='Quack'
    print(num1, num2, num3, num4, num5, num6, sep=',')

def entercard():
    global user
    user=int(input('Pick a card #: '))
def ifwin():
    global win
    if win == 2:
        print('You Won!')
        exit()

reprintcard()
entercard()

while count!=3:

    if user==1:                ##Check if it is one
        count+=1
        print('Card',user,' said Meow.')
        entercard()
        if user==3:
            print('Card ',user,' said Meow.')
            print('YAY!!! They match!')
            meow = 1
            win+= 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()
    elif user==2:                 ##Check if it is two
        print('Card ',user,' said Bark.')
        entercard()
        count+=1
        if user==6:
            print('Card ',user,' said Bark.')
            print('YAY!!! They match!')
            win+=1
            bark = 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()
    elif user==3:                 ##Check if it is 3
        print('Card ',user,' said Meow.')
        entercard()
        count+=1
        if user==1:
            print('Card ',user,' said Meow.')
            print('YAY!!! They match!')
            win+=1
            meow = 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()
    elif user==4:                 ##Check if it is 4
        print('Card ',user,' said Quack.')
        entercard()
        count+=1
        if user==5:
            print('Card ',user,' said Quack.')
            print('YAY!!! They match!')
            win+=1
            quack = 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()
    elif user==5:                 ##Check if it is 5
        print('Card ',user,' said Quack.')
        entercard()
        count+=1
        if user==4:
            print('Card ',user,' said Quack.')
            print('YAY!!! They match!')
            win+=1
            quack = 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()

    elif user==6:                 ##Check if it is 4
        print('Card ',user,' said Bark.')
        entercard()
        count+=1
        if user==2:
            print('Card ',user,' said Bark.')
            print('YAY!!! They match!')
            win+=1
            bark = 1
            ifwin()
            reprintcard()
            entercard()
        else:
            print('Sorry, Try again')
            win=0
            reprintcard()
            entercard()
    else:
        print('Enter a # between 1-6')
        entercard()
        reprintcard()
print('You won!!!')
