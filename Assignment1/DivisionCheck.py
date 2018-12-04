#This program reads an integer and prints
#whether is divisible by only 2 or divisible 
#by only 3 or divisible by neither or both 


#DivisionCheck.py


def main():
	

	inputNum= int(input("Enter an integer: "))
	if inputNum % 2==0 and inputNum % 3 == 0: #number divisible by both 2 and 3
		print("Number %d is divisible by both 2 and 3" %inputNum)

	elif inputNum % 2==0 and inputNum % 3 != 0: #number divisible by 2 but not 3
		print("Number %d is divisible by 2 but not 3" %inputNum)

	elif inputNum % 2 != 0 and inputNum % 3 ==0: #number divisible by 3 but not 2
		print("Number %d is divisible by 3 but not 2" %inputNum)

	else: #number divisible by neither 2 nor by 3
		print("Number %d is divisible by neither 2 nor by 3" %inputNum)





#Call main
main()