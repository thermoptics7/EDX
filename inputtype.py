#Recall that input from a user is always in the form of a string.
#Write a function  called "input_type" that gets user input and
#determines what kind of string the user entered.
#
#Note that because you're getting user input, you will not be able
#to run this code: the only way you can test it is to submit it.
#When you submit your code, we'll test it with some simulated
#input.
#
#  - Your function should return "integer" if the string only
#    contains characters 0-9.
#  - Your function should return "float" if the string only
#    contains the numbers 0-9 and at most one period.
#  - You should return "boolean" if the user enters "True" or
#    "False".
#  - Otherwise, you should return "string".
#
#Remember, start the input_type() function by getting the user's
#input using the input() function. The call to input() should be
#*inside the* input_type() function.


#Write your function here!
def input_type():
    userString = input("Please input a string of characters: ")
    integerList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    floatList = ["."]
    booleanList = ["True","False"]
    intCounter = 0
    floatCounter = 0

    if userString in booleanList:
        return "boolean"
    else:
        for character in userString:
            if character in floatList:
                floatCounter += 1
            elif character in integerList:
                intCounter += 1

        if intCounter == len(userString):
            return "integer"
        elif floatCounter < 2:
            return "float"
        else:
            return "string"

print(input_type())