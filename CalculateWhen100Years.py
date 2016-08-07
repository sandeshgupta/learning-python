'''
Question Link - http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

import time

name = input('Please enter your name\n')
age = input('Please enter your age\n')
times = input('No Of Times \n')
year = time.strftime('%Y')

yearWhen100 =int(year) -int(age) + 100

print((str(yearWhen100)+'\n') * int(times))
