#Write a function called luckySevens() that takes in one
#parameter, a string variable named aStr. Your function
#should return True if there are exactly three '7's in aStr.
#If there are less than three  or more than three '7's, the
#function should return False.
#
#For example:
#  - luckySevens("happy777bday") should return True.
#  - luckySevens("h7app7ybd7ay") should also return True.
#  - luckySevens("happy77bday") should return False.
#  - luckySevens("h777appy777bday") should also return False.

#Write your function here!

def luckySevens(aStr):
    sevenCounter = 0
    for currentCharacter in aStr:
        if currentCharacter == "7":
            sevenCounter += 1
        else:
            continue

    if sevenCounter == 3:
        return True
    else:
        return False


#You can use these lines to test your code. They are not used
#for grading, so feel free to change them.

testStringTrue = "We like flying in a 787"
print(testStringTrue, luckySevens(testStringTrue))
testStringFalse1 = "happy77bday"
print(testStringFalse1, luckySevens(testStringFalse1))
testStringFalse2 = "h777app7y77bday"
print(testStringFalse2, luckySevens(testStringFalse2))