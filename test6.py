#Write a function called averageWordLength that takes as
#input a string called myString, and returns as output the
#average length of the words in the string.
#
#In writing this function, note the following:
#
# - You should account for consecutive spaces. A string like
#   "Hi   Lucy" is two words with an average length of 3.0
#   characters.
# - You should not assume the string starts with a letter.
#   A string like "  David" has one words with an average
#   length of 5.0 characters.
# - You should not count punctuation marks toward the
#   length of a word. A string like "Hi, Lucy" has two
#   words with an average length of 3.0 characters: the ,
#   after "Hi" does not count as a character in the word.
#   The only punctuation marks you need to handle are
#   these: . , ! ?
# - You may assume the only characters in the string are
#   letters, the punctuation marks listed above, and spaces.
# - If myString is not a string, you should instead return
#   the string, "Not a string".
# - If there are no words in myString, you should instead
#   return the string, "No words". This could happen for
#   strings like "" (an empty string) and ".,!?" (a string
#   of only punctuation marks). You may assume that any
#   of these punctuation marks will always be followed by
#   at least one space.
#
#Here are a few hints that might help you:
#
# - You can peak at the first character in myString with
#   myString[0]. If myString is "Hi, Lucy", then the value
#   of myString[0] is "H".
# - There are lots of ways you can do this. If you're
#   stuck, try taking a step back and thinking about the
#   problem from a fresh perspective.
# - The word count should equal the number of letters that
#   come immediately after a space or the start of the
#   string. The character count should simply equal the
#   number of characters besides spaces and punctuation
#   marks. The average word length should be character
#   count divided by word count.


#Write your function here!

myString = "Hi.?"


for i in range(0, len(myString)):
    if myString[i] == ("." or "," or "!" or "?"):
        print("That's not a letter")

    elif myString[i] == " ":
        print("That's a space")

    else:
        print(myString[i])

print(len(myString))




#When your function works, the following code should
#output:
#2.0
#3.0
#4.0
#Not a string
#No words

#print(averageWordLength("Hi"))
#print(averageWordLength("Hi, Lucy"))
#print(averageWordLength("   What   big spaces  you    have!"))
#print(averageWordLength(True))
#print(averageWordLength("?!?!?! ... !"))