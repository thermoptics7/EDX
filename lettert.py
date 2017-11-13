#Write two for each loops, one nested within the other, to count how many
#times the letter "t" (not case sensitive) occurs in the given list of
#strings. Print the resulting number.

#Additionally, print the current string every time a "t" (again, not case
#sensitive) is found.

givenStrings = ["Taylor Swift", "Twenty Two", "Georgia Tech"]
#givenStrings = ["Omar", "Hassan", "Yaseen"]

#Do not edit the code above this line.

#Write your code here!
tCount = 0
for currentString in givenStrings:
    #print(currentString)
    for currentCharacter in currentString:
        if currentCharacter == "T":
            tCount += 1
            print(currentString)
        elif currentCharacter == "t":
            tCount += 1
            print(currentString)

print(tCount)


