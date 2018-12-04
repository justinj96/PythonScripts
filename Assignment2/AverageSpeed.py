'''
This program calculates the
average speed of vehicles 
over a time period

AverageSpeed.py
'''

def main():

	#vehicles participating assigned to variable
	vehicleCount = input("Enter the number of vehicles participating: ")

	#input validation
	while (not vehicleCount.isdigit()): 
		print("Input is not a positive interger")
		vehicleCount = input("Enter the number of vehicles participating: ")

	#changes variable from str to int
	vehicleCount = int(vehicleCount)

	#hours traveled assigned to variable
	hoursTraveled = input("Enter the number of hours traveled: ")

	#input validation
	while (not hoursTraveled.isdigit()): 
		print("Input is not a positive integer")
		hoursTraveled = input("Enter the number of hours traveled: ")

	#changes variable from str to int
	hoursTraveled = int(hoursTraveled)

	#set calculations to nothing so
	#calculations can be displayed
	calculations = ""

	#outer loop for each vehicle
	for vehicles in range(1,vehicleCount+1):
		print()
		totalSpeed = 0

		#inner loop for number of hours
		for hours in range(1, hoursTraveled+1):
			#prints prompt for speed with 'vehicles' and 'hours' changing based on 
			#which vehicle and hour the loop is on
			print('Enter the avg. speed of vehicle', vehicles, 'during hour', hours, end=' ') 
			speedOfHour = eval(input(': ')) #asks user for average speed over given hour
			
			#input validation
			while speedOfHour < 1: 
				print('Enter the CORRECT avg. speed of vehicle', vehicles, 'during hour', hours, end=' ')
				speedOfHour = eval(input(': ')) #asks again for input if not a positive number
			
			#adds up input of average speed per each hour
			totalSpeed += speedOfHour
		
		#average speed calculation
		avgSpeed = totalSpeed/hoursTraveled

		#adds each vehicle calculation
		calculations += ("%4d %12.2f %10.2f\n" %(vehicles, totalSpeed, avgSpeed))

	#prints table with heading and calculations
	print("\nVehicle", "Total Speed", "Avg. Speed")
	print("=======", "===========", "==========")
	print(calculations)
	

main()