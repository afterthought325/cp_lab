# A program that allows users to create and use a "bank" account.
# It utilizes SQlite.
#
# Chaise Farrar
# 10/23/2014
#
#

def main():

    from sqlite3 import dbapi2 as sqlite    # Import SQlite API
    database = sqlite.connect('atminfo.db')      # Import Database
    data = database.cursor()
    # Create table if it doesnt exists
    data.execute("create table if not exists people (first_name varchar, \
                 last_name varchar, pin integer, checking real, \
                 saving real)")

    while True:
        print("""
  ____ _           _            ____              _
 / ___| |__   __ _(_)___  ___  | __ )  __ _ _ __ | | __
| |   | '_ \ / _` | / __|/ _ \ |  _ \ / _` | '_ \| |/ /
| |___| | | | (_| | \__ \  __/ | |_) | (_| | | | |   <
 \____|_| |_|\__,_|_|___/\___| |____/ \__,_|_| |_|_|\_\\""")
        check = input('Do you have an account? "yes" or "no"\n--->')
        try:
            if check == 'yes':
                break
            elif check == 'no':
                new_user(database)
                #break
            else:
                raise TypeError
        except TypeError:
            print("\nIncorrect input, try again.")
        for c in range(100):
            print("\n")
    while True:
        user_pin = int(input('Please enter PIN: '))
        if len(str((user_pin))) == 4:   #check for correct # of digits
            query = "select first_name, last_name, pin, checking, saving \
                     from people where pin=?"
            data.execute(query,[user_pin]) #Pull user info from database
            user_info = data.fetchone() #Place user info into tuple
            if user_info == 'none': #if no user exists ask again
                break
        else:
            print('Please enter a 4 digit number.')
        try:
            if user_pin == user_info[2]:
                break
            else:
                input("Pin not found, please try again")
        except TypeError:
            input("Pin not found, please try again")

    while True: # Give Menue to choose from
        choose = int(input('\n1. Inquiry \n' +
                           '2. Deposit to checking \n' +
                           '3. Deposit to savings \n' +
                           '4. Withdrawl from checking \n' +
                           '5. Withdrawl from savings \n' +
                           '6. Quit \n\n Please choose an option: '))
        if choose == 1: ##INQUIRY
            inquiry(user_info[3], user_info[4])
            input('\n Press any key to go back: ')

        elif choose == 2:  ## DEPOSIT TO CHECKING
            user_info[3] = deposit(user_info[3])
            input('\n Press any key to go back: ')

        elif choose == 3:  ##DEPOSIT TO SAVINGS
            user_info[4] = deposit(user_info[4])
            input('\n Press any key to go back: ')

        elif choose == 4:  ##WITHDRAWL FROM CHECKING
            chk_bal = withdrawl(user_info[3])
            input('\n Press any key to go back: ')

        elif choose == 5:  ## WITHDRAWL FROM SAVINGS
            sav_bal = withdrawl(user_info[4])
            input('\n Press any key to go back: ')

        elif choose == 6:  ##QUIT
            break
        else:
            print('Input is not valid.')
    main()





def inquiry(chk_bal,sav_bal):
    print('\n Checking balance: ', chk_bal)
    print('\n Savings balance: ',sav_bal)

def deposit(balance):
    dep = int(input('\n Please enter how much you want to deposit: '))
    balance += dep
    print('\n Your new balance is: ', balance)
    return balance

def withdrawl(balance):
    withdrawl = int(input('\n Please enter how much you want to withdrawl: '))
    while withdrawl > balance:
       print('\n You broke foo.')
       withdrawl = int(input('\n Please enter how much you want to \
                             withdrawl: '))
    balance = balance - withdrawl
    print('\n Your new balance is: ', balance)
    return balance

def new_user(database):
    for a in range(100):            # Clear Screen
        print('\n')
    print("Thank You for choosing Chaise Bank.\nWe hope enjoy doing business" +
          " with us!\n")
    input("We need a little information to set up your account. Press Enter" +
          " to begin.\n")
    first_name = input('What is your first name?\n--->')    # Get Name
    last_name = input('\nWhat is your last name?\n--->')    # Get Last Name
    pin=int(input('\nWhat would you like your PIN ' +
                  '(Personal Identification Number) to be?\n--->'))    # Set Pin
    checking=float(input('\nHow Much is your initial deposit to checking?' +
                         '\n--->'))   # Initial Checking Deposit
    # See if they want a Savings Account
    checkyes = 0
    while True:
        checkyes=input('\nDo you want a savings account? "yes" or "no"\n--->')
        if checkyes == ('yes' or 'Yes'):
            savings=float(input('\nHow Much is your initial deposit to' +
                                ' savings?\n--->'))    # Intial Savings Deposit
            break
        elif checkyes == ('no' or 'No'):
            savings=0
            break
        else:
            print('')

    cur = database.cursor()
    # Put information into Table
    try:
        cur.execute('insert into people values (?,?,?,?,?)', \
                    [first_name, last_name, pin, checking, savings])
    except NameError:
        cur.execute('insert into people values (?,?,?,?)', \
                    [first_name, last_name, pin, check])
    database.commit()
    input('Thank You for creating an Account. Hope you enjoy!\nPress Enter to Continue.')
    return

#def clear():
#    import os
#    os.system('clc' if os.name == 'nt' else 'clear')
#    return ''
main()
