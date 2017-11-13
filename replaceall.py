#Write a function called "replace_all" that accepts three
#arguments:
#
# - targetString, a string in which to search.
# - findString, a string to search for.
# - replaceString, a string to use to replace every instance
#   of the value of find.
#
#The arguments will be provided in this order. Your function
#should mimic the behavior of "replace", but you cannot use
#that function in your implementation. Instead, you should
#find the result using a combination of "split" and "join",
#or some other method.
#
#Hint: This exercise can be complicated, but it can also
#be done in a single short line of code! Think carefully about
#the methods we've covered.

#Write your function here!

def replace_all(targetString,findString,replaceString):
    if " " in targetString:
        targetList = targetString.split()
        #print(targetList) #Debug Code
        for index, word in enumerate(targetList):
            #print(index,word) Debug Code
            if word == findString:
                #print("It's hitting the 1st conditional") #Debug code
                targetList[index] = replaceString
            if word == findString + ",":
                #print("It's hitting the 2nd conditional") #Debug code
                targetList[index] = replaceString + ","
            else:
                #print("It's hitting the 3rd conditional") #Debug code
                continue
        targetString = " ".join(targetList)

    else:
        targetList = list(targetString)
        for index, character in enumerate(targetList):
            if character == findString:
                targetList[index] = replaceString
            else:
                continue
        targetString = "".join(targetList)

    return targetString
    

#You can uncomment the lines below to test your code, but
#you should comment them back out before submitting lest the
#autograder misinterpret them as an attempt to circumvent it.
#When your function works correctly, this should output,
#"In case I don't see ya, bad afternoon, bad evening, and bad
#night!".
#target = "In case I don't see ya, good afternoon, good evening, and good night!"
#find = "good"
#replace = "bad"
#print(replace_all(target, find, replace))

#target = "Omar Sharieff ate a leaf, Omar then kept it brief, Omar then queefed!"
#find = "Omar"
#replace = "Nagger"
#print(replace_all(target, find, replace))

target = "Hey, JoeJoe, how are you?"
find = "JoeJoe"
replace = "Joe"
print(replace_all(target, find, replace))

#target = "ha!!!"
#find = "!"
#replace = ""
#print(replace_all(target, find, replace))

