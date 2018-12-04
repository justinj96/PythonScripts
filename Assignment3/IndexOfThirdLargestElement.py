'''
This program generates a random list of 20 numbers
then displays the third largest number and its index
IndexOfThirdLargestElement.py
'''

import random

def main():

	randNumList = randNumGen(1,40) #runs function to generate random numbers
	print("List of integers:", randNumList) #displays list of numbers
	pThird, num = returnIndex(randNumList) #sends list to function which finds number and index
	print("Third Largest Number:", num) #displays third largest number
	print("Index of third largest number:", pThird) #displays index of said number

def randNumGen(a,b):

	randNum = [] #empty list
	for i in range(20): #loops through 20 iterations 
		randNumList = random.randint(a,b) #generates numbers between 1-50
		randNum.append(randNumList) #adds number to list
	return randNum #sends generate

def returnIndex(x):

	y = list(x) #creates copy of orginally generated list
	y.sort() #sorts copy of list
	num = y[17] #finds 3rd largest number
	print(y)

	if num in x: #searchs orgignal list for 3rd largest number
		pThird = x.index(num) #gives index of number
	return pThird, num #sends index and number to main

main()
