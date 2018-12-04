'''
Program generates a sales file called Sales.txt
'''

outputFile = "Sales.txt"
from random import uniform
def main():

    #open file
    outFile = openFile()

    #Write file
    writeFile(outFile)

    #close file
    closeFile(outFile)

def openFile():

    #opens file to be written to and returns to main func
    outFile = open(outputFile, 'w')
    return outFile

def writeFile(outFile):

    #gather user input for number of weeks and people
    people = input("How many sales people?: ")
    while (not people.isdigit()):  
        people = input("How many sales people?: ")
    people = eval(people)

    weeks = input("How many weeks of sales?: ")
    while (not weeks.isdigit()):
        weeks = input("How many weeks of sales?: ")
    weeks = eval(weeks)
    

    #generate numbers and write to lines in text file
    for i in range(people):
        
        if i > 0: 
            outFile.write("\n") #adds new line after each line is written

        #writes random numbers to file
        for x in range(weeks):
            num = (round(uniform(1.0,200.0),2))
            numStr = str(num)
            outFile.write(numStr + ",")
    
    print("File successfully created")

def closeFile(outFile):

    outFile.close()

main()

