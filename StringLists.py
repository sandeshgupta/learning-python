'''
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
'''

def isPalindrome(stringToCheck):
	#A simple way to do it would be to reverse the string using reverse()
	#There will be two variable i and j keeping track of start and end of the string
	# Variable 'i' will move ahead and 'j' will move backward with each iteration
	#In each iteration char at 'i' will be compared to 'j'.
	#This will carry on until the middle of string is reached. If middle of string is reached by both 'i' and 'j', string is Palindrome. Middle of the string for any string will be when i==j (odd no of characters in string) or i== j-1 (even no of characters in string)

		
	#j is given assigned to last position of the string
	j = len(stringToCheck)-1

	#the loop will run from 0th position to mid of the string
	for i in range(0,j//2+1):
		if i<=j and  stringToCheck[i] == stringToCheck[j]: 
			if i==j or i==j-1: 
				return True
			j -= 1
			continue
		else: 
			return False


if __name__ =='__main__':
	#User input String
	stringToCheck = str(input('Enter a string\n'))
        
	isPalindromeResult = isPalindrome(stringToCheck)
	if isPalindromeResult == True:
		print('The string \''+stringToCheck+'\' is Palindrome')
	else:
		print('The string \''+stringToCheck+'\' is NOT Palindrome')


