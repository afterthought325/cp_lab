# ###############################################################################
# Name: Chaise Farrar       Date Assigned:10/29/2014                           #
# Course: CSE 1284 Sec 10   Date Due: 10/29/2014                               #
# Project Name: Art Gallery                                                    #
# Program Description: Program allows the creation and modification of an Art  #
# Gallery database.                                       #
# ###############################################################################
from sys import exit  # import for exit() command


class rpgCharacter:  # RPG Character Class
    def __init__(self, name, hp, damage):  # sets initial attributes
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        #the rest of the methods just return the values

    def getName(self):
        return self.__name

    def getHP(self):
        return self.__hp

    def getDamage(self):
        return self.__damage

    def getAll(self):
        return self.__name, self.__hp, self.__damage


def main():
    while True:  # Main Menu / Loop through
        # Program starts by reading file holding stats.
        # Next a loop reads each line after the first line is read.
        # It then strips the newline char, splits it into a list,
        # and creates an object given the values from the line. This
        # object is then stored in a dictionary called char.
        infile = open("fileio.txt", "r")
        trashline = infile.readline()
        char = {}
        f = 0
        for line in infile:
            line = line.strip().split(",")
            char[f] = rpgCharacter(line[0], int(line[1]), int(line[2]))
            f += 1
        infile.close()

        while True:  # Ask user for option. Loops till input valid
            try:  # Checks for non numbers
                menu_option = int(input('1. List Characters \n' +
                                        '2. Compare Characters \n' +
                                        '3. Create Character \n' +
                                        '4. Quit \n\nPlease choose an option: '))
                if menu_option in [1, 2, 3, 4]:  # check valid option
                    break  # Exits Validation loop
                else:  # else raise error and ask again
                    raise ValueError
            except ValueError:  # catch error, prompt user, loop
                print('Please enter the numerical values for the option.\n')


        if menu_option == 1:  # prints character information
            for c in char:  # sets the key from char to c to use to call that object definition
                print()
                print(char[c].getName())
                print('HP:', char[c].getHP())
                print('Damage:', char[c].getDamage())
                print()
            input("Press ENTER to return")
            print()


        elif menu_option == 2:  # compares characters
            print('The current list of Characters is:')
            for c in char:
                print(c, '. ', char[c].getName(), sep='')
            while True:
                c1 = int(input('Please choose your first option: '))
                c2 = int(input('Please choose your second option: '))
                if c1 in range(len(char)) and c2 in range(len(char)):
                    break
                else:
                    input("INVALID INPUT")
            if char[c1].getHP() > char[c2].getHP():
                difference_of_hp = char[c1].getHP() - char[c2].getHP()
                print(char[c1].getName(), "has", difference_of_hp, 'more hp than', char[c2].getName())
            else:
                difference_of_hp = char[c2].getHP() - char[c1].getHP()
                print(char[c2].getName(), "has", difference_of_hp, 'more hp than', char[c1].getName())
            if char[c1].getDamage() > char[c2].getDamage():
                difference_of_damage = char[c1].getDamage() - char[c2].getDamage()
                print(char[c1].getName(), "has", difference_of_damage, 'more damage than', char[c2].getName())
            else:
                difference_of_damage = char[c2].getDamage() - char[c1].getDamage()
                print(char[c2].getName(), "has", difference_of_damage, 'more damage than', char[c1].getName())
            input('\n\nPress ENTER to return')
            print('\n')


        elif menu_option == 3:  # Creates new character
            while True:  # loops till valid name given
                newcharactername = input("Name of Character: ")
                if "," not in newcharactername:  # checks for commas
                    break
                else:
                    print("Name cannot have commas\n\n")
            while True:  # loops till valid HP given
                try:  # stops non integers from being input
                    newcharacterhp = int(input("Amount of HP: "))
                    break
                except ValueError:
                    input("HP must be an integer\n\n")
            while True:  # loops till valid Damage given
                try:  # stops non integers from being input
                    newcharacterdamage = int(input('Damage Power: '))
                    break
                except ValueError:
                    input("Must be an integer\n\n")
            outfile = open('fileio.txt', 'a')
            newcharacter = '\n' + newcharactername + ',' + str(newcharacterhp) + ',' + str(newcharacterdamage)
            outfile.write(newcharacter)
            outfile.close()


        elif menu_option == 4:  # quit
            c = input("Are you sure? (yes or no): ")
            while True:
                if c in ['y', 'Y', 'Yes', 'yes']:
                    exit(1)
                else:
                    break


main()