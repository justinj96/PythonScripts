'''
This program takes three points
of a triangle and displays the area

AreaOfTriangle.py
'''

def main():

	#input of points
	x1,y1 = eval(input("Enter point 1 (x1, y1) for the triangle: ")) 

	x2,y2 = eval(input("Enter point 2 (x2, y2) for the triangle: ")) 

	x3,y3 = eval(input("Enter point 3 (x3, y3) for the triangle: ")) 


	#compute individual sides
	sideA = (((x2 - x1)**2) + ((y2 - y1)**2)) ** .5

	sideB = (((x3 - x2)**2) + ((y3 - y2)**2)) ** .5

	sideC = (((x3 - x1)**2) + ((y3 - y1)**2)) ** .5


	#first part of area equation
	semi = (sideA + sideB + sideC)/2

	#final part of area equation
	area = (semi * (semi - sideA) * (semi - sideB) * (semi - sideC)) ** .5

	#displays area of triangle
	print()
	print("Area of the triangle is: %.2f" %area)

#Call main
main()