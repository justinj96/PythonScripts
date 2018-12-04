#program reads the contents of a file and counts how often words appear

outputFile = "WordFreq.txt"
def main():

    #open
    userFile = openFile()

    #process
    processData(userFile)

    #close
    close(userFile)
   
def openFile():
    
    whichFile = input("Enter file name: ") #get user input
    
    #look for file name, ask to re-enter if it doesn't exist
    try:
        userFile = open(whichFile, 'r')
    except FileNotFoundError:
        whichFile = input("Input file not found. Please re-enter: ")

    userFile = open(whichFile, 'r')
    return userFile
    
def processData(userFile):
    outFile = open(outputFile, 'w')
    numberOfWords = {}
    print()
    totalCount = 0
    #add key and value to dict
    for word in userFile.read().split():
        word = word.strip(",.'!?-;:").lower() #strip strings of punctuation
        if word not in numberOfWords: #check if word is already in dict
            #see if string is a float or int, ignore if it is
            try: 
                float(word)
                continue
            #added to dict if not float or int
            except ValueError:
                numberOfWords[word] = 1
                totalCount += 1  
        else: #if already in dict, add to counter
            numberOfWords[word] += 1
            totalCount += 1

    print(numberOfWords) #print dict to command line
    print()

    #write to command line and file
    for key in sorted(numberOfWords): #for key in dict
        outFile.write(key)
        outFile.write(" ")
        count = str(numberOfWords[key]) #convert count to string to be written to file
        outFile.write(count)
        outFile.write("\n")

        #print key and individual count to command line
        print("%s %d" %(key, numberOfWords[key]))

    print()
    print("Total number of words = ", totalCount)
    totalCount = str(totalCount)
    outFile.write("Total number of words = ")
    outFile.write(totalCount)

    outFile.close()
def close(userFile):
    userFile.close()

main()