#program that shows course information in a dictionary

def main():

    #show user course options
    print()
    print("Courses")
    print("=======")
    print("MIS120\nMIS15\nMIS101\nMIS150\nMIS160")
    userEntry = getCourseNumber()

    getInstructor(userEntry)

    getMeetingTime(userEntry)


def getCourseNumber():

    print()
    userEntry = input("Enter a course number: ").upper()
    #room dictionary
    courseRoom = {
        'MIS120' : 'TAH1009',
        'MIS15' : 'ALP224',
        'MIS101' : 'AMD132',
        'MIS150' : 'TAH1026',
        'MIS160' : 'ARC1013'
    }

    #input validation
    while userEntry not in courseRoom:
        print("Invalid Course Number")
        userEntry = input("Enter a valid course number: ").upper()

    #display room based on input key
    print("Room:", courseRoom[userEntry])
    return userEntry


def getInstructor(userEntry):

    #instructor dictionary
    courseInstructor = {
        'MIS120' : 'Beverly Smith',
        'MIS15' : 'Casey Woods',
        'MIS101' : 'Lisa Burton',
        'MIS150' : 'Violet Jenkins',
        'MIS160' : 'Troy Curtis'
    }
    #display instructor based on input key
    print("Instructor:", courseInstructor[userEntry])

def getMeetingTime(userEntry):

    #time dictionary
    courseTime = {
        'MIS120' : '6:00pm',
        'MIS15' : '1:30pm',
        'MIS101' : '9:00am',
        'MIS150' : '12:00pm',
        'MIS160' : '4:30pm'
    }

    #display time based on input key
    print("Meeting Time:", courseTime[userEntry])


main()  