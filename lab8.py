################################################################################
# Name: Chaise Farrar       Date Assigned:10/29/2014                           #
# Course: CSE 1284 Sec 10   Date Due: 10/29/2014                               #
# Project Name: Art Gallery                                                    #
# Program Description: Program allows the creation and modification of an Art  #
#                      Gallery database.                                       #
################################################################################

def main():
    title = ['Stuff','Chaise']
    genre = ['Artsy','WTH']
    artist = ['Chaise','Chaise']
    year = [3453,2000]
    value = [12234235,50495]
    all_lists = [title,genre,artist,year,value]
    print('Hello, Welcome to the MSU Art Gallery Admin Database.')
    while True:     ##presents MAIN MENU
        while True: ##Ask user for option. Loops till input valid
            try:    ##Checks for non numbers
                choice = int(input('1. Insert Artwork \n'+  #Prints menu
                                   '2. Find Most Valued Artwork \n' +
                                   '3. Find Least Valued Artwork \n' +
                                   '4. Show Average Value of Artwork \n' +
                                   '5. Delete Artwork \n' +
                                   '6. Find Artwork By Title\n' +
                                   '7. Find Artwork By Year.\n' +
                                   '8. Quit \n\nPlease choose an option: '))
                if choice in [1,2,3,4,5,6,7,8]:  #check valid option
                    break   #Exits Validation loop
                else:  #else raise error and ask again
                    raise ValueError
            except ValueError:#catche error, prompt user, loop
                input('Please enter the numerical values for the option.\n \
                       Press ENTER to continue...')
        if choice == 1:
            while True:# Loops back around if the user choses to use
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
                    break
        elif choice == 2:
            try:
                c = value.index(max(value))
            except:
                input("ERROR: Max not found")
                raise SystemExit(0)
            print(title[c])
            print(genre[c])
            print(artist[c])
            print(year[c])
            print(value[c])
            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 3:
            try:
                c = value.index(min(value))
            except:
                input("ERROR: Min not found")
                raise SystemExit(0)
            print(title[c])
            print(genre[c])
            print(artist[c])
            print(year[c])
            print(value[c])
            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 4:
            print(sum(value)/len(value))
            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 5:
            while True:
                delete = input('What is the name of the artwork you \
                                want to delete:')
                try:
                    delete in title
                    c = title.index(delete)
                    for a in range(len(all_lists)):
                        all_lists[a].remove(c)
                    repeat=input('Do you want to delete another? \
                                 "yes" or "no"')
                    if repeat in ["yes","y","Y","Yes"]:
                        pass
                    else:
                        break
                except ValueError:
                    print('Artwork not found')
            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 6:
            while True:
                find_art = input('What is the name of the artwork you \
                                  want to find:')
                try:
                    find_art in title
                    c = title.index(find_art)
                    for a in range(len(all_lists)):
                        print(all_lists[a][c])
                    break
                except ValueError:
                    print('Artwork not found')
            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 7:
            while True:
                find_art = int(input('What is the year of the artwork you \
                                      want to find:'))
                try:
                    find_art in year
                    c = year.index(find_art)
                    for a in range(len(all_lists)):
                        print(all_lists[a][c])
                    break
                except ValueError:
                    print('Artwork not found.')

            input('Press anything to return...')
            print('\n\n\n\n\n')
        elif choice == 8:
            raise SystemExit(0)
        else:
            print('FATAL ERROR: COMMAND NOT FOUND')
            raise SystemExit(0)
main()
