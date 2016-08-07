'''
Link : http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
'''

#Initialising the list
a = [1,3,5,66,2,4,8,8,90,5,4]
print('Initial List = ', a)

#looping through list
print('Elements which are less than 5')
for i in a:
	#check eack element for condition less than 5
	if i < 5:
		print(i,',',end ="")


#Extra Point No 1

#New list will contain numbers less than 5
b = []
for i in a:
	if i<5:
		b.append(i);
print('\nElements which are less than 5. Output as List\n',b)


#Extra Point no 2
#List comprehension
print('Element less than 5 in one line\n',[i for i in a if i<5] )


#Extra Point No 3
number = int(input('Enter a number '))
print('Element less than %d \n'%(number) ,[i for i in a if i<number])

