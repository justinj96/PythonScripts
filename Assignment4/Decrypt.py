'''
Program to decrypt a encrypted text file
'''
inputFile = "EncryptedEmail.txt"
outputFile = "Decrypted.txt"
#This program looks very similar to Encrypt.py
#but actually is Decrypt.py

def main():

    #open file
    inFile = openFile()

    #write encryption list based on key
    orgList, decrypt = en(inFile)
    
    #write encrypted email
    write(inFile, orgList, decrypt)
    
    #close
    inFile.close()
    

def openFile():

    inFile = open(inputFile, 'r')
    return inFile

def en(inFile):

    #encryption scheme
    orgList = ['a','b','c','d','e','f','g','h','i','j','k','l','m',\
    'n','o','p','q','r','s','t','u','v','w','x','y','z',\
    'A','B','C','D','E','F','G','H','I','J','K','L','M',\
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    #create copy of scheme to keep the original intact
    decrypt = list(orgList)

    #user input of key and input validation
    key = input("Enter the encryption/decryption key: ")
    while (not key.isdigit()):
        key = input("Input invalid. Enter the encryption/decryption key: ")
    key = int(key)
    
    #slice ranges of key from alphabet
    listSlice = decrypt[0:key]
    listSliceU = decrypt[26:key+26]
    
    #insert slice into proper place
    counter = 0
    for char in listSlice:
        decrypt.insert(26+counter,char)
        counter += 1

    for char in listSliceU:
        decrypt.append(char)
        del decrypt[26+key]

    #delete newly inserted section from old location
    del decrypt[0:key]

    return orgList, decrypt


def write(inFile, orgList, decrypt):

    #string concatenation to write decrpted lines to command line
    displayDecrypted = ("")
    inFile = inFile.read()
    for ch in inFile:
        if ch in decrypt:
            chIn = decrypt.index(ch) #grab index from decrypt
            displayDecrypted += orgList[chIn] #add character at that index to decrypted string
        else:
            displayDecrypted += (ch) #if not in scheme add directly to string (spaces, commas, apostrophes, \n)
    
    encrypted = open(inputFile,'r')
    displayEncrypted = encrypted.read() #read encrypted file

    #display encrypted file
    print()
    print("Encrypted File:")
    print(displayEncrypted)
    print()
    
    #display decrypted file
    print()
    print("Decrypted File:")
    print(displayDecrypted)
    print()

    encrypted.close()

main()