def averageWordLength(myString):
    charCounter = 0
    charCountRegister = 0
    spaceCounter = 0
    wordCounter = 0
    punctuationList = [".", ",", "!", "?"]
    try:
        for character in myString:
            if character == " ": #looking for spaces
                if charCounter != 0:
                    spaceCounter += 1
                    charCountRegister += charCounter #using this counter register method to ensure we catch consecutive spaces that may appear in a string
                    wordCounter += 1
                    charCounter = 0
                else:
                    #pass
                    spaceCounter += 1 #most likely to occur if a string begins with space(s)
            elif character in punctuationList: #ignores anything in the punctuation list
                pass
            else:
                charCounter += 1 #counts characters if it wasn't a space or punctuation

    except TypeError: #exception handling for non-strings that may get passed
        return "Not a string"

    if charCounter == 0: #handles strings that con't containy words
        if charCountRegister == 0:  # catches strings that don't have any words
            return "No words"
        else: #handles the case where a string ends with a bunch of spaces
            charCountRegister += charCounter
            result = charCountRegister / wordCounter

    elif spaceCounter == 0: #accounts for one-word strings
        charCountRegister = charCounter
        wordCounter = 1
        result = charCountRegister / wordCounter
        #print("# of Characters is: ", charCounter)
        #print("Character Register is: ", charCountRegister)
        #print("# of Words is: ", wordCounter)
        #print("# of Spaces is: ", spaceCounter)
        #print("Average WL1 is: ", averageWordLength)

    else: #handles a string with multiple words and no spaces at the end.
        wordCounter += 1
        charCountRegister += charCounter
        result = charCountRegister / wordCounter

        #print("# of Characters is: ", charCounter)
        #print("Character Register is: ", charCountRegister)
        #print("# of Words is: ", wordCounter)
        #print("# of Spaces is: ", spaceCounter)
        #print("Average WL2 is: ", averageWordLength)

    #NOTE: Need to account for the case where a string end logically but there are spaces at the end of the logical string.

    return result

#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

print(averageWordLength("Hi"))
print(averageWordLength("Hi, Lucy"))
print(averageWordLength("   What   big spaces  you    have!"))
print(averageWordLength(True))
print(averageWordLength("?!?!?! ... !"))
#print(averageWordLength(""))
#print(averageWordLength("One space. Two spaces.  Three spaces.   Nine spaces.         "))