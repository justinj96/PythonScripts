'''
this program displays grade distribution
DetermineGrade.py
'''

import random

def main():

	score = generateScores(50.0, 100.0)
	lengthA, lengthB, lengthC, lengthD, lengthF = determineGrade(score)
	

	#displays formatted table
	print("%7s %15s %11s" %("Score", "Letter Grade", "# Students"))
	print("=========","==============","============")
	#displays first two columns which always stay the same
	#and displays number of students
	print("%7s %9s %12s" %("90.0-100", 'A', lengthA))
	print("%7s %8s %12s" %("80.0-89.9", 'B', lengthB))
	print("%7s %8s %12s" %("70.0-79.9", 'C', lengthC))
	print("%7s %8s %12s" %("60.0-69.9", 'D', lengthD))
	print("%5s %12s %12s" %("<60.0", 'F', lengthF))

#generate scores using uniform and append
def generateScores(a, b):
	randScores = []
	for i in range(40): #iterates 40 times
		scores = random.uniform(a,b)
		randScores.append(scores) 
	return randScores

#Determines grades based on test score 
#using the length function
def determineGrade(testScore):
	#each list variable adds numbers between given values to list
	#each length gives length of the list to be sent to main

	aList = [x for x in testScore if 90.0 <= x <= 100.0] 
	lengthA = len(aList)

	bList = [x for x in testScore if 80.0 <= x <= 89.9]
	lengthB = len(bList)

	cList = [x for x in testScore if 70.0 <= x <= 79.9]
	lengthC = len(cList)
	
	dList = [x for x in testScore if 60.0 <= x <= 69.9]
	lengthD = len(dList)

	fList = [x for x in testScore if 0.0 <= x <= 59.9]
	lengthF = len(fList)
	
	#sends number of students back to main function
	return lengthA, lengthB, lengthC, lengthD, lengthF
	



#Call main
main()