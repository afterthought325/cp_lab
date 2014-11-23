################################################################################
# Name: Chaise Farrar       Date Assigned:10/16/2014                           #
# Partner: Rebecca Siciliano                                                   #
# Course: CSE 1284 Sec 10   Date Due: 10/16/2014                               #
# File name:ATM Machine                                                        #
# Program Description: Simulates an ATM experiance, from logging in with       #
#                      a pin to checking acount balance                        #
################################################################################
import getpass
def main():
    checking_balance = 50000
    saving_balance = 10000
    pin = int(getpass.getpass('\nHello! Welocome! Please enter your four digit PIN: '))

    while pin == 7894:
        while True:
            try:
                choose = int(input('\n1. Inquiry \n'+
                                   '2. Deposit to checking \n' +
                                   '3. Deposit to savings \n' +
                                   '4. Withdrawl from checking \n' +
                                   '5. Withdrawl from savings \n' +
                                   '6. Quit \n\nPlease choose an option: '))
            except ValueError:
                print('Input is not valid.')
                raise SystemExit(0)

            if choose == 1:
                inquiry(checking_balance,saving_balance)
                input('\n Press any key to go back: ')
            elif choose == 2:
                checking_balance = deposit(checking_balance)
                input('\n Press any key to go back: ')
            elif choose == 3:
                saving_balance = deposit(saving_balance)
                input('\n Press any key to go back: ')
                break
            elif choose == 4:
                checking_balance = withdrawl(checking_balance)
                input('\n Press any key to go back: ')
                break
            elif choose == 5:
                saving_balance = withdrawl(saving_balance)
                input('\n Press any key to go back: ')
            elif choose == 6:
                print('Thank You for your Business')
                raise SystemExit(0)
    print('\n Unknown PIN.')
    input('\n Press any key to go back: ')
    main()

def inquiry(checking_balance,saving_balance):
    print('\n Checking balance: ',checking_balance)
    print('\n Savings balance: ',saving_balance)

def deposit(balance):
    dep = int(input('\n Please enter how much you want to deposit: '))
    balance += dep
    print('\n Your new balance is: ', balance)
    return balance

def withdrawl(balance):
    withdrawl = int(input('\n Please enter how much you want to withdrawl: '))
    while withdrawl > balance:
       print('\n You broke foo.')
       withdrawl = int(input('\n Please enter how much you want to withdrawl: '))
    balance = balance - withdrawl
    print('\n Your new balance is: ', balance)
    return balance

main()
