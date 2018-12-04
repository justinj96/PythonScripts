'''
This program calculates the projected
increase of tuition over a 
specified number years

TuitionIncrease.py
'''

def main():

	#user input for current tuition fee
	tuitionFee = float(input("Enter the current tuition fee: "))

	#input validation
	while tuitionFee < 1:
		print("INVALID INPUT: TUITION FEE SHOULD BE GREATER THAN 0")
		tuitionFee = float(input("Enter the current tuition fee: "))

	#user input for percent increase
	increasePercentage = float(input("Enter the percent increase: "))
	
	#input validation
	while increasePercentage < 1:
		print("INVALID INPUT: PERCENT INCREASE SHOULD BE GREATER THAN 0")
		increasePercentage = float(input("Enter the percent increase: "))

	#user input for number of years
	timePeriod = float(input("Enter the number of years: "))
	
	#input validation
	while timePeriod < 1:
		print("INVALID INPUT: NUMBER OF YEARS SHOULD BE GREATER THAN 0")
		timePeriod = float(input("Enter the number of years: "))

	#displays header
	print("\nYear", "\tProjected Tuition (per Semester)")
	print("----------------------------------------")

	#count controlled loop 
	#iterates as many times as years input
	for year in range(1,timePeriod+1):

		#calculates tuition increase for each year
		tuitionIncrease = tuitionFee * increasePercentage/100

		#add tuition increase to previous tuition 
		tuitionFee += tuitionIncrease

		#displays projected tuition for each year 
		print("%d \t$%.2f" %(year, tuitionFee))
		
#call main
main()
