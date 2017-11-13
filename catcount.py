#This one is tricky! Think carefully about for-each loops, conditionals, and
#strings. How can you track what character you're currently looking for?

#Write a for each loop that counts how many times the word "cat" occurs in
#mysteryString. Print the result.
mysteryString = "my cat your cat"
#Don't modify the code above!
#When you run your code, we'll test it with the string "my cat your cat".
#When you Submit your code, we'll test it with some other strings, too.
cCount = 0
aCount = 0
tCount = 0
catCount = 0

for currentCharacter in mysteryString:
    if currentCharacter == "c":
        if cCount == 0:
            cCount += 1
        else:
            cCount = 1

    if currentCharacter == "a":
        if cCount == 1:
            aCount += 1
        else:
            aCount = 0

    if currentCharacter == "t":
        if cCount == 1:
            if aCount == 1:
                catCount += 1
                cCount = 0
                aCount = 0
                tCount = 0




print("This string has",catCount, "cats")




