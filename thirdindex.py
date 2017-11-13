#Write function called third_index that accepts a string
#as an argument and returns just the third character of
#the string. Ifthe user inputs a string with fewer than
#3 characters, return "too short".


#Write your function here!
def third_index(myString):
    if len(myString) >= 3:
        #print("1st conditional")
        #print(myString[2])
        #returnString = myString[2]
        return myString[2]

    else:
        #print("else")
        #print("too short")
        #returnString = "too short"
        return "too short"




#If you want to write any test cases to test your code,
#you can write them below!

#third = third_index("Yo why you playin son!!!")
#print(third)

#third = third_index("wtf")
#print(third)

#third = third_index("no")
#print(third)

third = third_index('Taylor Swift')
print(third)

third = third_index('a')
print(third)

