'''
Program computes average sales for each 
sales person and for each week
Data taken from text file sales.txt
USE CREATESALES.PY TO CREATE SALES.TXT
'''
inputFile = "Sales.txt"

def main():

    #open
    inFile = openFile()

    #process
    processData(inFile)

    #close
    close(inFile)

def openFile():

    inFile = open(inputFile, 'r')
    return inFile
    
def processData(inFile):

    salesPersonList = []
    floatList = []
    for line in inFile:
        salesPersonList.append(line.strip().strip(',').split(",")) #adds numbers to list
    for num in salesPersonList: #for each number in the list
        floatList.append([float(i) for i in num]) #iterate through each string, convert to float, add to new list
    
    #creates list were lists inside are groups of sales for each week
    weeksList = []
    for i in range(len(line)):
        try:
            weeksList.append([(item[i]) for item in floatList])
        except:
            continue

    print("\nWeek ", " Total Sales ", " Average Sales ")
    
    #calculate and print table for sales per week
    total = 0.0
    average = 0.0
    for i in range(len(weeksList)):
        total = sum(weeksList[i])
        average = total/len(weeksList[i])

        #print each week's calculations
        print("%3d %12.2f %13.2f" %(i+1,total,average))

    print("\nSales Person ", " Total Sales ", " Average Sales ")

    #calculate and print table for sales per person
    total = 0.0
    average = 0.0
    for i in range(len(floatList)):
        total = sum(floatList[i])
        average = total/len(floatList[i])

        #printing each persons calculations
        print("%6d %17.2f %13.2f" %(i+1,total,average))

    print()

def close(inFile):

    inFile.close()

main()