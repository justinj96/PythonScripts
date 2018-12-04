'''
This program computes the BMI of a person

ComputeBMI.py
'''

def main():

	#input weight and height
	weight = float(input("Enter weight in pounds: "))
	feet,inches = eval(input("Enter height in (feet,inches): "))

	#One pound = 0.45359237 Kilograms 
	#One inch = 0.0254 Meters
	
	#conversion constants
	poundToKgs = 0.45359237
	inchesToMeters = 0.0254
	
	#convert weight from pounds to kg
	weightInKilograms = weight * poundToKgs
	
	
	#convert height to meters
	#converting user input to inches
	heightInInches = (feet * 12) + inches
	#converting inches to meters
	heightInMeters = heightInInches * inchesToMeters
	

	#given bmi formula
	bmi = (weightInKilograms) / (heightInMeters * heightInMeters)

	#displays formatted BMI
	print("Your BMI is: %.1f" %bmi)

	if (bmi <= 18.5):
		print("You are Underweight")
	elif (bmi > 18.5) and (bmi < 24.9):
		print("You are Normal" )
	elif (bmi > 25) and (bmi < 29.9):
		print("You are Overweight")
	else: 
		print("You are Obese")
	
#call main
main()