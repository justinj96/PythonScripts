'''
This program generates a count
of how many of an input amount of
integers are even and odd

EvenOddCounter.py
'''

#imports python module 'random'
import random

def main():

	#obtains user input for number 
	#of intergers to be generated
	intCount = input("Enter the number of random integers to be generated: ")
	
	#input validation
	while (not intCount.isdigit()): 
		print("Input is not a positive interger")
		intCount = input("Enter the number of random integers to be generated: ")

	#changes input from type str to int
	intCount = int(intCount)
	
	#receives even and odd counts from loop()
	evenCount, oddCount = loop(intCount)

	#displays count of even and odd numbers
	print("Out of 100 random numbers, %s were odd, and %s were even."\
		%(oddCount, evenCount))

#function loops and generates random numbers
#to be counted as even or odd
def loop(x):

	#set count of even numbers to 0
	evenCount = 0

	#set count of odds to 0
	oddCount = 0

	#loop for as many times as users input
	for i in range(1,x+1):
		#random number between 1 and 100
		r = random.randint(1,101)

		#To check if random number is even
		if(r % 2 == 0):
			evenCount+=1
		else:
			oddCount+=1

	#sends even and odd count to main function
	return evenCount, oddCount

#call main
main()