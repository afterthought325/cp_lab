import random

def main():
    c = 'y'
    while c == 'y':
        u1 = dc()
        u2 = dc()
        u3 = -1
        c1 = dc()
        c2 = dc()
        c3 = -1
        print("User:", GcV(u1), "", GcV(u2), end='')
        if u3 != -1:
            print("", GcV(u3), end='')
        print("\nComputer:", GcV(c1), "", GcV(c2), end='')
        if c3 != -1:
            print("", GcV(c3), end='')
        print("\n")
        us = SC_HA(u1, u2, u3)
        cs = SC_HA(c1, c2, c3)
        u3 = a()
        us = SC_HA(u1, u2, u3)
        if us > cs and us <= 21:
            c3 = dc()
        #print("User:", GcV(u1), "", GcV(u2), end='')
        if u3 != -1:
            print("", GcV(u3), end='')
            print("\nComputer:", GcV(c1), "", GcV(c2), end='')
        cs = SC_HA(c1, c2, c3)
        if c3 != -1:
            print("", GcV(c3), end='')
            print("\n")

        print("User score: ", us)
        print("Computer score: ", cs)
        if us < 21:
            print("Busted!")
        elif us == cs:
            print("It's a tie")
        elif cs <= 21 and cs > us:
            print("Sorry. You lost!")
        else:
            print("Congratulations! You won.")
        c = input("Do you want to play again?")
        if c != 'y' and c !='n':
            print("Please enter only a 'y' or 'n'")
            c = input("Do you want to play again?")
def dc():
    return random.randint(0,51)
    
def GcV(card):
    faceValue = int(card / 4) + 1
    suit = card % 4
    if faceValue == 0:
        faceValue = ""
    elif faceValue == 1:
        faceValue = "A"
    elif faceValue == 11:
        faceValue = "J"
    elif faceValue == 12:
        faceValue = "Q"
    elif faceValue == 13:
        faceValue = "K"
    else:
        faceValue = str(faceValue)
    if suit == 0:
        suit = " Clubs  "
    elif suit == 1:
        suit = " Diamonds  "
    elif suit == 2:
        suit = " Hearts  "
    elif suit == 3:
        suit = " Spades  "
    else:
        suit == ''
        print("Error! Bad suit")
    return faceValue + suit
def SC_HA(card1, card2, card3):
    score = 0
    faceValue1 = int(card1 / 4) + 1
    faceValue2 = int(card2 / 4) + 1
    faceValue3 = 0
    if card3 != -1:
        faceValue3 = int(card3 / 4) + 1
    if faceValue1 == 0:
        score1 = 0
    elif faceValue1 == 1:
        score1 = 11
    elif faceValue1 == 11 or faceValue1 == 12 or faceValue1 == 13:
        score1 = 10
    else:
        score1 = faceValue1    
    if faceValue2 == 0:
        score2 = 0
    elif faceValue2 == 1:
        score2 = 11
    elif faceValue2 == 11 or faceValue2 == 12 or faceValue2 == 13:
        score2 = 10
    else:
        score2 = faceValue2
    if faceValue3 == 0:
        score3 = 0
    elif faceValue3 == 1:
        score3 = 11
    elif faceValue3 == 11 or faceValue3 == 12 or faceValue3 == 13:
        score3 = 10
    else:
        score3 = faceValue3
    score = score1 + score2 + score3
    return score

def a():
    an = input("Would you like one more card? (y/n) ")
    while an != 'y' and an != 'n':
        print("Please enter 'y' or 'n'")
        an = input("Would you like one more card? (y/n) ")
    if an == 'y':
        return dc()
    else:
        return -1
    
main()
