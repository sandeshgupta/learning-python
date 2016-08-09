'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''

#Taking input a number from user
number = int(input('Enter a number\n'))

#This will store all the divisors
divisors = [];

#This will loop through a list(list consists of all the numbers from 0 to number/2) 
for i in range(1, (number//2) + 1):
	if number % i ==0:
		divisors.append(i)

#As the list consisted of numbers from 0 to number/2, the number itself wasn't checked.Hence, adding it manually
divisors.append(number)

print(divisors)

