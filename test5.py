#This exercise is identical to the previous exercise,
#except that instead of printing "Cannot convert!" when myVar
#cannot be converted to an integer, you should instead print
#the error message that results. For a reminder of how to
#access the error message in the except block, check out
#3.5.3, specifically CatchingASpecificError-4.py from 3.5.3.3
#and CatchingMultipleSpecificErrors-5.py from 3.5.3.4.
#
#Write a function called getInteger that takes as input one
#variable, myVar. If myVar can be converted to an integer,
#do so and return that integer. If myVar cannot be converted
#to an integer, return the error message that results from
#attempting to do so.
#
#Do not use any conditionals.


#Write your function here!
def getInteger(myVar):
    try:
        result = int(myVar)
        return result

    except Exception as error:
        return error

#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#invalid literal for int() with base 10: 'Boggle.'
#5
print(getInteger("5"))
print(getInteger("Boggle."))
print(getInteger(5.1))
