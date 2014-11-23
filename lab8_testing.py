################################################################################
# Name: Chaise Farrar       Date Assigned:10/29/2014                           #
# Partner: Rebecca Siciliano                                                   #
# Course: CSE 1284 Sec 10   Date Due: 10/29/2014                               #
# Project Name: Art Gallery                                                    #
# Program Description: Program allows the creation and modification of an Art  #
#                      Gallery database.                                       #
################################################################################
def main():
    print('Hello, Welcome to the MSU Art tGallery Admin Database.\n\n\n')
    while True:     ##presents MAIN MENU
        while True: ##Asks for which option user wants. Loops till valid input is given
            try:    ##Checks for non numbers
                choice = int(input('1. Insert Artwork \n'+  #Prints menu
                                   '2. Find Most Valued Artwork \n' +
                                   '3. Find Least Valued Artwork \n' +
                                   '4. Show Average Value of Artwork \n' +
                                   '5. Delete Artwork \n' +
                                   '6. Find Artwork By Title\n' +
                                   '7. Find Artwork By Year.\n' +
                                   '8. Quit \n\nPlease choose an option: '))
                if choice ==[1,2,3,4,5,6,7,8]:  #check if number is valid option
                    break   #Exits Validation loop
                else:
                    raise ValueError    #else raise error to loop back and ask again
            except ValueError:  #catches errors, prompts user, loops to ask again
                input('Please enter the numerical values for the option.\n' +
                      'Press ENTER to continue...')
        options={1:in_art(),  #dictionary to pair option chosen to name of function
                 2:find_max(),
                 3:find_min(),
                 4:avg(),
                 5:delete(),
                 6:find_title(),
                 7:find_year(),
                 8:quit()
                }
       options[choice]

def in_art():
    while True:
        while True:
            try:
                title.append(input('Title:'))
                genre.append(input('Genre:'))
                artist.append(input('Artist Name:'))
                year.append(int(input('Year:')))
                value.append(int(input('Value:')))
                break
            except ValueError:
                input('Incorrect input.')
        c = input('\n\nDo you want to add another piece of art?\n \
                      "yes" or "no"')
        if c in ['No','no','NO','n']:
            return

main()
