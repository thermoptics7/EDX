#Create a program that divides 10 by mysteryValue and prints
#the result. In the case that mysteryValue is equal to 0,
#print "Not possible". In the case that mysteryValue is not
#a number, print "Not a number".

#You may not use any conditionals.

mysteryValue = "Omar"

#Do not edit anything above this line! When you click Run,
#we'll run your code with mysteryValue = 9. When you click
#Submit, we'll run your code with a few other values as well.
try:
    result = 10 / mysteryValue
    print(result)

except ZeroDivisionError as error:
    #print("Not possible")
    print(error)


except TypeError as error:
    #print("Not a number")
    print(error)



