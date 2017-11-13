def averageWordLength(myString):
    charCounter = 0
    #charCountRegister = 0
    spaceCounter = 0
    wordCounter = 0
    punctuationList = [".", ",", "!", "?"]
    try:
        for character in myString:
            if character == " ":
                if charCounter != 0:
                    spaceCounter += 1
                    #charCountRegister += charCounter
                    wordCounter += 1
                    #charCounter = 0
                else:
                    pass
            elif character in punctuationList:
                pass
            else:
                charCounter += 1
    except TypeError:
        return "Not a string"

    if spaceCounter == 0:
        if charCounter == 0:
            if charCountRegister == 0:
                return "No words"
        else:
            charCountRegister = charCounter
            wordCounter = 1
            result = charCountRegister / wordCounter
            #print("# of Characters is: ", charCounter)
            #print("Character Register is: ", charCountRegister)
            #print("# of Words is: ", wordCounter)
            #print("# of Spaces is: ", spaceCounter)
            #print("Average WL1 is: ", averageWordLength)
    else:
        wordCounter += 1
        charCountRegister += charCounter
        result = charCountRegister / wordCounter

        print("# of Characters is: ", charCounter)
        print("Character Register is: ", charCountRegister)
        print("# of Words is: ", wordCounter)
        print("# of Spaces is: ", spaceCounter)
        print("Average WL2 is: ", averageWordLength)

    return result
#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

#print(averageWordLength("Hi"))
print(averageWordLength("Hi, Lucy"))
#print(averageWordLength("   What   big spaces  you    have!"))
#print(averageWordLength(True))
#print(averageWordLength("?!?!?! ... !"))
#print(averageWordLength(""))
#print(averageWordLength("One space. Two spaces.  Three spaces.   Nine spaces.         "))