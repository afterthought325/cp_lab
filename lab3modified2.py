

print('Please enter the ISBN # one digit at a time. Disregard any dashes.\n')
count = 0
isbn = list(map(int, input('Please Enter The ISBN #, no dashes please!\n--->')))
a = isbn[0]+isbn[2]+isbn[4]+isbn[6]+isbn[8]+isbn[10]+(3*(isbn[1]+isbn[3]+isbn[5]+isbn[7]+isbn[9]+isbn[11])) #add odd digits and add,multiply by three even digits
a = a % 10
print('The check digit is: ', isbn[12])       ##Print the entered check digit
if a == 0:  ##Check if the check digit is zero, then print
    print('The calculated check digit is: ', a)
else:   ##if not, calculate check digit by subtracting total from 10, then print
    total = 10 - a
    print('The calculated check digit is:', total)
