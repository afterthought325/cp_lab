# Name: Chaise Farrar       Date Assigned:9/17/2014
#
# Course: CSE 1284 Sec 10   Date Due: 9/17/2014
#
# File name:Valid ISBN
#
# Program Description: Enter ISBN # and calculate the check digit, then compare to the actual check digit.

print('Please enter the ISBN # one digit at a time. Disregard any dashes.\n')

num1 = int(input('Enter a Digit: '))  #Enter each number one at a time
num2 = int(input('Enter a Digit: '))
num3 = int(input('Enter a Digit: '))
num4 = int(input('Enter a Digit: '))
num5 = int(input('Enter a Digit: '))
num6 = int(input('Enter a Digit: '))
num7 = int(input('Enter a Digit: '))
num8 = int(input('Enter a Digit: '))
num9 = int(input('Enter a Digit: '))
num10 = int(input('Enter a Digit: '))
num11 = int(input('Enter a Digit: '))
num12 = int(input('Enter a Digit: '))
num13 = int(input('Enter a Digit: '))

print('The check digit is: ',num13)       ##Print the entered check digit

##Calculate the Check digit based on entered ISBN
total = num1+num3+num5+num7+num9+num11+(3*(num2+num4+num6+num8+num10+num12)) #add odd digits and add then multiply even digits
total = total%10  ##Get the remainder of the total

if total == 0:  ##Check if the check digit is zero, then print
    print('The calculated check digit is: ',total)
else:   ##if not, calculate check digit by subtracting total from 10, then print
    checkDigit = 10 - total
    print('The calculated check digit is:',checkDigit)
