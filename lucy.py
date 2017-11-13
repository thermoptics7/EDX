#This may be a tough one. You can do it!
#
#You'll have access to a variable called mysteryString. On subsequent
#lines, your code should print the first character, then the first
#two characters, then the first three characters, and so on, until
#it prints the entire string on the last line. For example, if the
#string was "Lucy", then the output would be:
#
#L
#Lu
#Luc
#Lucy
mysteryString = "HassanYaseenSharieff"
#Don't modify the code above!
#Write your code here. You'll have access to a variable named mysteryString,
#which will be a string. When you Run, we'll test your code with "Lucy" as
#the mysteryValue. When you Submit, we'll test it with some other values.

for i in range(1,len(mysteryString)+1):
    for j in range(0, i):
        print(mysteryString[j], end = "")
        #print(mysteryString[j])
    print()


