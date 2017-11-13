#Write a function called getInteger that takes as input one
#variable, myVar. If myVar can be converted to an integer,
#do so and return that integer. If myVar cannot be converted
#to an integer, return a message that says, "Cannot convert!"
#
#For example, for "5" as the value of myVar, getInteger would
#return the integer 5. If the value of myVar is the string
#"Boggle.", then getInteger would return a string with the
#value "Cannot convert!"
#
#Do not use any conditionals.

#Write your function here!

def getInteger(myVar):
    try:
        result = int(myVar)
        return result

    except:
        return "Cannot convert!"





#You can use the lines below to test out your function. When
#the function is written correctly, the output of these three
#lines should be:
#5
#Cannot convert!
#5

print(getInteger("5"))
print(getInteger("Boggle."))
print(getInteger(5.1))
#print(getInteger("Omar"))