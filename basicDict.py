programmer_dict = {"tim berners-lee":['tbl@gmail.com', 111],
                        "guido van rossum":['gvr@gmail.com', 222],
                        "linus torvalds": ['lt@gmail.com', 333],
                        "larry page": ['lp@gmail.com', 444],
                        "sergey brin": ['sb@gmail.com', 555]}

for key in programmer_dict:
        print (key.title())

print('')

def searchPeople(personName):
        try:
            personInfo = programmer_dict[personName]
            print "Name: " + personName.title()
            print "Email: " + personInfo[0]
            print "Number: " + str(personInfo[1])
        except:
            print "No information found for that name."
            
userWantsMore = True

while userWantsMore == True:
    personName = raw_input("Please enter the full name of a programmer above for contact info: ").lower()
    searchPeople(personName)
    searchAgain = raw_input("Would you like to search another name?: y/n").lower()
    if searchAgain == "y":
       userWantsMore = True
    elif searchAgain == "n":
        userWantsMore = False
        print "Goodbye."
    else:
        userWantsMore = False
        print "Invalid input. Goodbye." 

