'''
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1.    Randomly generate two lists to test this
2.    Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
'''


def getUniqueCommonList(a,b):
        #First, it will loop through list a.
        #For each element of a, it will check if element of 'a' is present in 'b'. If it is present in both, then it's a common element
        #Then, it will check if that common element is present in list 'c', which contains common element without duplicates
	
	c=[]

	for i in a:
		if i in b:
			if i not in c:
                                c.append(i)
	return c



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#This will store common unique elements
c= getUniqueCommonList(a,b)

print('First List:',a,'\nSecond List:',b,'\nCommon unique elements between both lists are: ',c)		


#Extras. No 1.

import random

#Store random number in a list of random length
a1 = []
noOfItemsA1 = int(random.random()*10)

b1 = []
noOfItemsB1 = int(random.random()*10)

#Generating random numbers in list
for x in range(1,noOfItemsA1):
	a1.append(random.randrange(1,100,1))

for x in range(1,noOfItemsB1):
        b1.append(random.randrange(1,100,1))

print('\nExtras No 1. \nFirst List:',a1,'\nSecond List:',b1,'\nCommon unique elements between both lists are: ',getUniqueCommonList(a1,b1))


#Extras. No 2.

print('\nExtras No 2. In one line \nFirst List:',a,'\nSecond List:',b,'\nCommon unique elements between both lists are: ',
set(a) & set(b)
)









