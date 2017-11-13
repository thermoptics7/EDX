#Write a for-each loop that lists each character in
#mysteryString with its index. For example, if the
#string was "abc", the output would be:
#1 a
#2 b
#3 c
#
#Hint: You'll need a separate variable to keep track
#of how many letters you've printed!

#Don't modify the code above!

#Write your code here. When you Run your code, we'll test it with
#mysteryString = "CS1301". When you Submit your code, we'll test it
#with a couple other strings.

myString = "Boyaakashaaaaaaa"
charCount = 0
for currentChar in myString:
    charCount += 1
    print(charCount,currentChar)