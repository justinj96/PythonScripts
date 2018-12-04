'''
Program that uses a key to encrypt a text file
Use Decrypt.py to decrypt
'''
inputFile = "Email.txt"
outputFile = "EncryptedEmail.txt"

def main():

    #open file
    inFile = openFile()

    #write encryption list based on key
    orgList, encrypt, key = en(inFile)
    
    #write encrypted email
    write(inFile, orgList, encrypt, key)
    
    #close
    inFile.close()
    

def openFile():

    #open file
    inFile = open(inputFile, 'r')
    return inFile

def en(inFile):

    #scheme
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m',\
    'n','o','p','q','r','s','t','u','v','w','x','y','z',\
    'A','B','C','D','E','F','G','H','I','J','K','L','M',\
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #dulpicate list
    encrypt = list(orgList)

    #key input and input validation
    key = input("Enter the encryption/decryption key: ")
    while (not key.isdigit()):
        key = input("Input invalid. Enter the encryption/decryption key: ")
    key = int(key)
    
    #slice ranges of key from scheme
    listSlice = encrypt[0:key]
    listSliceU = encrypt[26:key+26]
    
    #insert slice into proper place to create encryption code
    counter = 0
    for char in listSlice:
        encrypt.insert(26+counter,char) 
        counter += 1

    for char in listSliceU:
        encrypt.append(char)
        del encrypt[26+key]

    #delete newly inserted section
    del encrypt[0:key]

    return orgList, encrypt, key


def write(inFile, orgList, encrypt, key):
    
    #open file to be written to
    outFile = open(outputFile, 'w')

    #write encrypted file
    inFile = inFile.read()
    for ch in inFile:
        if ch in orgList:
            chIn = orgList.index(ch) #grab index from orgList
            outFile.write(encrypt[chIn]) #write character at index to encrypted file
        else:
            outFile.write(ch) #if not in scheme add directly to file (spaces, commas, apostrophes, \n)
    
    #displays to command line to ensure that the program worked
    #also reminds the user of the key they entered to be used in Decrypt.py
    print("File Successfully written")
    print("Remember your key, it is needed to decrypt the file")
    print("Your key is:", key)

    outFile.close()


main()