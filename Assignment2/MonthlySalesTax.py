'''
This program calculates state, 
federal, and total sales tax


MonthlySalesTax.py
'''

#global variables for state and 
#federal sales tax rates
stateTaxRate = .05
federalTaxRate = .025

def main():
	
	#user input for total sales
	totalSales = eval(input("Enter the total sales for the month: $"))
	#input validation
	while totalSales < 1 :	 
		print("INVALID INPUT")
		totalSales = eval(input("Please enter a positive numeric value for total sales: $"))
	
	#pass totalSales through to state()
	stateTax = state(totalSales)
	#pass totalSales through to federal()
	federalTax = federal(totalSales)
	#pass stateTax and federalTax through to total()
	totalTax = total(stateTax,federalTax)

	#displays all calculations
	print("State Tax: $%.2f" %stateTax)
	print("Federal Tax: $%.2f" %federalTax)
	print("Total Tax: $%.2f" %totalTax)

#function for state tax calculation
#total sales passed to 'revenue'
def state(revenue):
	#state tax calculated
	stateTax = stateTaxRate * revenue
	return stateTax
	#state tax calculation sent to main()

#function for federal tax calculation
#total sales passed to 'revenue'
def federal(revenue):
	#federal tax calculated
	federalTax = federalTaxRate * revenue
	return federalTax
	#federal tax calulation sent to main()

#function for total tax calculation
#state tax and federal tax passed through 's' and 'f'
def total(s,f):
	#total tax calculated
	totalTax = s + f
	return totalTax
	#total tax sent to main()


#call main
main()