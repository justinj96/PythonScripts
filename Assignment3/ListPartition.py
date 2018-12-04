'''
This program moves items around so values less than or equal to pivot
are in front and values greater than pivot are to the right
ListPartition.py
'''

import random

def main():

	#run function to generate 20 random numbers between 1-20
	originalList = createList(1,50) 
	print('Original List') #displays heading
	print(originalList) #displays generated list

	#get pivot value from user
	pivotValue = int(input('Enter the pivot value: '))
	#validate
	while (pivotValue not in originalList):
		pivotValue = int(input('Value not in list, enter new value: '))

	#send original list and pivot value to partitionList function
	lessThanList = partitionList(pivotValue, originalList) 
	print('Partitioned List') #displays heading
	print(lessThanList) #displays partitioned list

def createList(a,b):
	#NOTE: the original assignment said to get a list from the user 
	#but you said we should just make this function a random list generator

	randNum = [] #empty list
	for i in range(20): #loops through 20 iterations 
		originalList = random.randint(a,b) #generates numbers between 1-50
		randNum.append(originalList) #adds number to list
	return randNum #sends generated list back to function

def partitionList(pivot, inputList):
	
	lessThanList = [] #empty list for values less than pivot value
	greaterThanList = [] #empty list for values greater than pivot value
	pivotList = [] #empty list for values equal to pivot

	for i in range(len(inputList)):
		if inputList[i] < pivot: #if value less than pivot
			lessThanList.append(inputList[i]) #add to lessThanList
		if inputList[i] > pivot: #if value greater than pivot
			greaterThanList.append(inputList[i]) #add to greaterThanList
		if inputList[i] == pivot: #if value equal to pivot 
			pivotList.append(inputList[i]) #add to pivotList

	lessThanList.extend(pivotList) #add values equal to pivot to end of numbers less than pivot
	lessThanList.extend(greaterThanList) #add values greater than pivot to end of list
	return lessThanList #return final list to main

main()

