'''
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into 		num, tell that to the user. If not, print a different appropriate message.

'''

number = int(input('Enter a number\n'))

if number%4 == 0 :
	print('Div by 4')
elif (number % 2) == 0  : 
	print('Even')
else:
	print('Odd')



number = int(input('Enter number \n'))
check = int(input('Enter check \n'))

if number % check == 0:
	print('div')
else:
	print('non div')
