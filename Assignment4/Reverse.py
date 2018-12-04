'''
Program reads each line from a file and 
writes them in reveres order to another file
'''


inputFile = "input.txt"
outputFile = "output.txt"
def main():

    #open file
    inFile = open(inputFile, 'r')
    #process
    processData(inFile)
    #close
    inFile.close()

def processData(inFile):

    #open output.txt in write mode
    outFile = open(outputFile, 'w')

    #add lines to list and split by spaces
    lines = []
    for line in inFile:
        lines.append(line.split())

    #reverse each word
    for lst in lines:
        lst.reverse()
        
        #write the word and a space to the file
        for word in lst:
            outFile.write(word)
            outFile.write(" ")
        
        #at the end of each line add a new line
        outFile.write("\n")

    #display confirmation of file be created
    #close output file
    print("File 'output.txt' created")
    outFile.close()



main()